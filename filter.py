import os
import re
import pprint
import json
import spacy
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


def read_file(path: str) -> str:
    """
    Args:
        path: Path to a file.

    Returns:
        File contents as a string.
    """
    with open(path) as file:
        return file.read()


def preprocess_docstring(docstr: str, tag: str) -> List[str]:
    """
    Args:
        docstr: Docstring of a query.
        tag: Desiered part of speech tag.

    Returns:
        List of tokens of the docstring that has the given pos tag.
    """

    tokens = nlp(docstr)
    pos_tags = [token.tag_ for token in tokens]

    # checks whether the word has expected pos tag
    tokens = [tokens[i] for i, pos in enumerate(pos_tags) if pos == tag]
    tokens = [token.lemma_ for token in tokens]

    return tokens


def check_exists(docstr: str, words: List[str], tag: str = 'VB') -> bool:
    """
    Args:
        docstr: Docstring of a query.
        words: List of verbs connected to the given action verb.
        tag: Desiered part of speech tag.

    Returns:
        True if any of the words exists in the docsting, otherwise False.
    """

    tokens = preprocess_docstring(docstr, tag)
    exists = [np.any(word in tokens) for word in words]

    if np.any(exists):
        return True
    return False


def filter_by_verbs(data: str, verbs: List[str]) -> list:
    """
    Args:
        data: Docstrings of a queries.
        verbs: All the verbs connected to the given action verb.

    Returns:
        List of queries where the verb exists in the docstring.
    """

    data = '[' + re.sub(r'\}\s\{', '},{', data) + ']'
    data = json.loads(data)

    verb_data = []
    for i, file in tqdm(enumerate(data), total=len(data), desc='Processing code search net queries.'):
        exists = check_exists(file['docstring'], verbs)
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
        data = read_file(file)
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
        exists = check_exists(file['docstring'], words=prepositions, tag='IN')
        if exists:
            data_list.append(file)

    save_to_json(data_list, out_path)


def ccg_parse_filtered_functions(file_path: str, out_path: str):
    """
    Args:
        file_path: Path to the json/jsonl file to be processed.
        out_path: Path to the json/jsonl file to save results in.

    Gets the ccg parses to dicstrings, adds them to the dataframe and save as json/jsonl file.
    """

    df = read_json(file_path)

    df['ccg_parse'] = ''
    for i, file in tqdm(df.iterrows(), total=len(df), desc="Processing filtered queries."):
        try:
            tree = parse_sentence(file['docstring'])
            parse_str = get_ccg_parse(tree)
            parse_str = postprocess_parse(parse_str)

            df.at[i, 'ccg_parse'] = parse_str
        except Exception:
            pass

    save_to_json(df, out_path)


if __name__ == '__main__':
    # all_verbs = get_strings_from_predicate('convert')
    # get_code_search_net_files(all_verbs, file_path='../code_search_net/train', out_path='../code_search_net/train_filtered.jsonl.gz')

    # prepositions = ['to', 'into', 'from']
    # filter_by_preposition(prepositions, file_path='../code_search_net/train_filtered.jsonl.gz',
    #                       out_path='../code_search_net/train_filtered_preposition.jsonl.gz')

    ccg_parse_filtered_functions(file_path='../code_search_net/train_filtered.jsonl.gz',
                                 out_path='../code_search_net/train_filtered_parses.jsonl.gz')
