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


def get_all_verbs_from_action_verb(action_verb: str) -> List[str]:
    """Returns all the verbs related to the provided action verb."""

    verb = f'${action_verb.capitalize()}'
    verb_list = [k for k, v in STRING2PREDICATE.items() if v[0] == verb]

    if verb_list:
        return verb_list
    raise ValueError(f'The action word {action_verb} is not in the predicate dictionary.')


def list_files(directory: str, file_ext: str = '.jsonl') -> List[str]:
    """List all files in the given directory (recursively)."""
    filenames = []

    for root, dirs, files in os.walk(directory):
        for filename in files:
            if filename.endswith(file_ext):
                filenames.append(os.path.join(root, filename))

    return filenames


def read_file(filename: str) -> str:
    """Open a file and return its contents as a string."""
    with open(filename) as file:
        return file.read()


def preprocess_docstring(docstr: str, tag: str) -> List[str]:
    """Tokenizing and lemmatizing the docstring of the function."""

    tokens = nlp(docstr)
    pos_tags = [token.tag_ for token in tokens]

    # checks whether the word is a verb or not
    tokens = [tokens[i] for i, pos in enumerate(pos_tags) if pos == tag]
    tokens = [token.lemma_ for token in tokens]

    return tokens


def check_exists(docstr: str, words: List[str], tag: str = 'VB') -> bool:
    """Checks whether any of the verbs exists in docsting."""

    tokens = preprocess_docstring(docstr, tag)
    is_prefix = [np.any(q_word in tokens) for q_word in words]

    if np.any(is_prefix):
        return True
    return False


def get_filtered_functions(data: str, verbs: List[str]) -> list:
    """Checks whether any of the verbs exists in docsting."""

    data = '[' + re.sub(r'\}\s\{', '},{', data) + ']'
    data = json.loads(data)

    verb_data = []
    for i, file in tqdm(enumerate(data), total=len(data), desc='Processing code search net queries.'):
        exists = check_exists(file['docstring'], verbs)
        if exists:
            verb_data.append(file)
    return verb_data


def save_to_json(data: List[dict], name: str):
    """Makes the dataframe and saves it to json/jsonl file."""

    df = pd.DataFrame.from_dict(data, orient='columns')
    df.to_json(name, orient='records', lines=True)


def read_json(path: str):
    """Reads the specfied json/jsonl file to pandas dataframe."""
    return pd.read_json(path, orient='records', lines=True)


def get_code_search_net_files(verbs: List[str], path: str = '../code_search_net/', partition: str = 'train'):
    """Gets all the files from a directory, filters out the necessary queries and saves them in json/jsonl file."""

    data_files = list_files(path + partition)
    data_list = []

    for file in data_files:
        data = read_file(file)
        funcs = get_filtered_functions(data, verbs)
        data_list.extend(funcs)

    save_to_json(data_list, name=f'{path}/{partition}_filtered.jsonl')


def filter_out_prepositions(prepositions: List[str], path: str = '../code_search_net/', partition: str = 'train'):
    """Gets the json/jsonl and filters out the functions with desired prepositions."""

    df = read_json(f'{path}/{partition}_filtered.jsonl')
    data_list = []

    for i, file in tqdm(df.iterrows(), total=len(df), desc='Processing filtered functions.'):
        exists = check_exists(file['docstring'], words=prepositions, tag='IN')
        if exists:
            data_list.append(file)

    save_to_json(data_list, name=f'{path}/{partition}_prepositions_filtered.jsonl')


def ccg_parse_filtered_functions(path: str = '../code_search_net/', partition: str = 'train', preposition: bool = False):
    """Gets the json/jsonl files, gets the ccg parses of every queries, adds to the dataframe and save as json/jsonl file."""

    if preposition:
        df = read_json(f'{path}/{partition}_prepositions_filtered.jsonl')
    else:
        df = read_json(f'{path}/{partition}_filtered.jsonl')

    df['ccg_parse'] = ''
    for i, file in tqdm(df.iterrows(), total=len(df), desc="Processing filtered queries."):
        try:
            tree = parse_sentence(file['docstring'])
            parse_str = get_ccg_parse(tree)
            parse_str = postprocess_parse(parse_str)

            file['ccg_parse'] = parse_str
        except Exception:
            pass

    if preposition:
        df = save_to_json(df, f'{path}/{partition}_prepositions_filtered_parses.jsonl')
    else:
        df = save_to_json(df, f'{path}/{partition}_filtered_parses.jsonl')


if __name__ == '__main__':
    # all_verbs = get_all_verbs_from_action_verb('Convert')
    # get_code_search_net_files(all_verbs, partition='train')
    # get_code_search_net_files(all_verbs, partition='valid')

    # prepositions = ['to', 'into', 'from']
    # filter_out_prepositions(prepositions, partition='train')

    ccg_parse_filtered_functions(partition='train')
