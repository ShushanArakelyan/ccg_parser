import os
import re
import json
import spacy
from spacy.tokens import Doc

import numpy as np
import pandas as pd

from tqdm import tqdm
from typing import List

from parser_dict import STRING2PREDICATE
from parser import parse_sentence, get_ccg_parse, postprocess_parse


nlp = spacy.load('en_core_web_sm')


def get_strings_from_predicate(action_verb: str) -> List[str]:
    """
    Args:
        action_verb: Desired action verb/predicate.

    Returns:
        List of verbs related to the action verb.
    """
    verb = f'${action_verb.capitalize()}'
    verb_list = [k for k, v in STRING2PREDICATE.items() if v[0] == verb]

    if verb_list:
        return verb_list
    raise ValueError(
        f'The action word {action_verb} is not in the predicate dictionary.')


def list_files(dir_path: str, file_ext: str = '.jsonl') -> List[str]:
    """
    Args:
        dir_path: Path to the directory.
        file_ext: Desired file extension.

    Returns:
        List of files in the given directory (recursively).
    """
    filenames = []

    for root, dirs, files in os.walk(dir_path):
        for filename in files:
            if filename.endswith(file_ext):
                filenames.append(os.path.join(root, filename))

    return filenames


def preprocess_docstring(docstr: str, tag: str) -> List[str]:
    """
    Args:
        docstr: Docstring tokens of a query.
        tag: Desiered part of speech tag.

    Returns:
        List of tokens of the docstring that has the given pos tag.
    """

    doc = ' '.join(docstr).lower()
    tokens = nlp(doc)
    pos_tags = [token.tag_ for token in tokens]

    # checks whether the word has expected pos tag
    tokens = [tokens[i]
              for i, pos in enumerate(pos_tags) if pos.startswith(tag)]
    tokens = [token.lemma_ for token in tokens]

    return tokens


def check_exists(docstr: str, words: List[str], tag: str) -> bool:
    """
    Args:
        docstr: Docstring tokens of a query.
        words: List of verbs connected to the given action verb.
        tag: Desiered part of speech tag.

    Returns:
        True if any of the words exists in the docsting, otherwise False.
    """

    tokens = preprocess_docstring(docstr, tag)
    exists = [np.any(token in words) for token in tokens]

    if np.any(exists):
        return True
    return False


def filter_by_verbs(data: str, verbs: List[str]) -> list:
    """
    Args:
        data: DataFrame of queries.
        verbs: All the verbs connected to the given action verb.

    Returns:
        List of queries where the verb exists in the docstring.
    """

    verb_data = []
    for i, file in tqdm(data.iterrows(), total=len(data), desc='Processing code search net queries.'):
        exists = check_exists(file['docstring_tokens'], verbs, tag='VB')
        if exists:
            verb_data.append(file)
    return verb_data


def save_to_json(data: List[dict], path: str):
    """
    Args:
        data: List of dictionaries with filtered queries.
        path: The path to the json/jsonl file to save results in.
    """

    df = pd.DataFrame.from_dict(data, orient='columns')
    df.to_json(path, orient='records', lines=True)


def read_json(path: str):
    """
    Args:
        path: The path to the directory with CodeSearchNet data.

    Returns:
        Reads the specfied json/jsonl file to pandas dataframe.
    """
    return pd.read_json(path, orient='records', lines=True)


def get_code_search_net_files(verbs: List[str], file_path: str, out_path: str):
    """
    Args:
        verbs: All the verbs connected to the given action verb.
        file_path: Path to the directory with the CodeSearchNet data.
        out_path: Path to the json/jsonl file to save results in.
    """

    data_files = list_files(file_path)
    data_list = []

    for file in data_files:
        data = read_json(file)
        funcs = filter_by_verbs(data, verbs)
        data_list.extend(funcs)

    save_to_json(data_list, out_path)


def filter_by_preposition(prepositions: List[str], file_path: str, out_path: str):
    """
    Args:
        prepositions: All the prepositions to filter out.
        file_path: Path to the json/jsonl file to be processed.
        out_path: Path to the json/jsonl file to save results in.
    """

    df = read_json(file_path)
    data_list = []

    for i, file in tqdm(df.iterrows(), total=len(df), desc='Processing filtered functions.'):
        exists = check_exists(file['docstring_tokens'],
                              words=prepositions, tag='IN')
        if exists:
            data_list.append(file)

    save_to_json(data_list, out_path)


def ccg_parse_filtered_functions(file_path: str, out_path: str, logdir: str, time_limit: int = 15):
    """
    Args:
        file_path: Path to the json/jsonl file to be processed.
        out_path: Path to the json/jsonl file to save results in.
        logdir: Path to save txt reports in.
        time_limit: The maximum time parsing can take.

    Gets the ccg parses to dicstrings, adds them to the dataframe and save as json/jsonl file.
    """

    df = read_json(file_path)
    df['ccg_parse'] = ''
    parsed_q_count = 0

    # created the directory if absent
    if not os.path.exists(logdir):
        os.mkdir(logdir)

    with open(logdir + '/failed_queries.txt', 'w') as f_out, \
            open(logdir + '/exceptions.txt', 'w') as ex_out, \
            open(logdir + '/timeout.txt', 'w') as t_out:
        data_gen = tqdm(df.head(5).iterrows(), total=len(
            df), desc="Processing filtered queries.")
        for i, file in data_gen:
            doc = ' '.join(file['docstring_tokens']).lower()
            try:
                parse_tree = parse_sentence(doc, time_limit=time_limit)
                parse_str = get_ccg_parse(parse_tree)
                parse_str = postprocess_parse(parse_str)

                df.at[i, 'ccg_parse'] = parse_str
                parsed_q_count += 1
            except StopIteration:
                f_out.write("{} {} \n".format(doc, i))
                f_out.flush()
            except TimeoutError:
                t_out.write("{} {} \n".format(doc, i))
                t_out.flush()
            except Exception as ex:
                ex_out.write("{} {} \n".format(doc, i))
                ex_out.write(str(ex))
                ex_out.flush()

            data_gen.set_description("Success rate: {:.2f}".format(
                float(parsed_q_count) / len(df)), refresh=True)

    save_to_json(df, out_path)


if __name__ == '__main__':
    # all_verbs = get_strings_from_predicate('convert')
    # get_code_search_net_files(all_verbs, file_path='../code_search_net/valid',
    #                           out_path='../code_search_net/valid_filtered_pos1.jsonl.gz')

    # prepositions = ['to', 'into', 'from']
    # filter_by_preposition(prepositions, file_path='../code_search_net/train_filtered.jsonl.gz',
    #                       out_path='../code_search_net/train_filtered_preposition.jsonl.gz')

    ccg_parse_filtered_functions(file_path='../code_search_net/train_token.jsonl.gz',
                                 out_path='../code_search_net/train_parsed.jsonl.gz',
                                 logdir='../code_search_net/train_parse')
