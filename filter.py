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
from parser import get_wordnet_pos, parse_sentence

nlp = spacy.load("en_core_web_sm")


def get_all_verbs_from_action_verb(action_verb: str) -> List[str]:
    """Returns all the verbs related to the provided action verb."""

    verb = f'${action_verb.capitalize()}'
    verb_list = [k for k, v in STRING2PREDICATE.items() if v[0] == verb]

    if verb_list:
        return verb_list
    raise ValueError(
        f'The action word {action_verb} is not in the predicate dictionary.')


def list_files(directory: str, file_ext: str = ".jsonl") -> List[str]:
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
    for i, file in tqdm(enumerate(data[:10]), total=len(data), desc="Processing code search net functions."):
        exists = check_exists(file['docstring'], verbs)
        if exists:
            verb_data.append(file)
    return verb_data


def save_to_csv(data: List[dict], name: str):
    """Makes the dataframe and saves it to csv file."""

    df = pd.DataFrame.from_dict(data, orient='columns')
    df.to_csv(name)


def read_csv(path: str):
    """Reads the specfied csv file to pandas dataframe."""
    return pd.read_csv(path)


def get_code_search_net_files(verbs: List[str], path: str = '../code_search_net/', partition: str = 'train'):
    """Gets all the files from a directory, filters out the necessary functions and saves them in csv."""

    data_files = list_files(path + partition)
    data_list = []

    for file in data_files:
        data = read_file(file)
        data_list.extend(get_filtered_functions(data, verbs))

    save_to_csv(data_list, name=f'{path}/{partition}_filtered.csv')


def filter_out_prepositions(prepositions: List[str], path: str = '../code_search_net/', partition: str = 'train'):
    """Gets the csv and filters out the functions with desired prepositions."""

    df = read_csv(f'{path}/{partition}_filtered.csv')
    data_list = []

    for i, file in tqdm(df.iterrows(), total=len(df), desc="Processing filtered functions."):
        exists = check_exists(file['docstring'], words=prepositions, tag='IN')
        if exists:
            data_list.append(file)

    save_to_csv(
        data_list, name=f'{path}/{partition}_prepositions_filtered.csv')


def ccg_parse_filtered_functions(path: str = '../code_search_net/', partition: str = 'train', preposition: bool = False):
    """Gets the csv and gets the proportion of parsable docstrings."""

    proportion = 0
    if preposition:
        df = read_csv(f'{path}/{partition}_prepositions_filtered.csv')
    else:
        df = read_csv(f'{path}/{partition}_filtered.csv')

    for i, file in tqdm(df.iterrows(), total=len(df), desc="Processing filtered functions."):
        try:
            parse_sentence(file['docstring'])
        except Exception:
            proportion += 1

    print(f'For {partition} with preposition {preposition} is {((len(df) - proportion) / len(df)) * 100}%')


if __name__ == "__main__":
    # all_verbs = get_all_verbs_from_action_verb('Convert')
    # get_code_search_net_files(all_verbs, partition='train')
    # get_code_search_net_files(all_verbs, partition='valid')

    # prepositions = ['to', 'into', 'from']
    # filter_out_prepositions(prepositions, partition='valid')

    ccg_parse_filtered_functions(partition='valid')
