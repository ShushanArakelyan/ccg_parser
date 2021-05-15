import copy
import logging
import os
import signal
import string

import numpy as np
import stanza
from nltk.ccg import chart, lexicon
from nltk.corpus import wordnet
from nltk.stem import WordNetLemmatizer
from nltk.tag.stanford import StanfordPOSTagger
from spacy.lang.en import English
from spacy.tokenizer import Tokenizer

from parser_dict import STRING2PREDICATE, WORD2NUMBER, RAW_LEXICON, QUESTION_WORDS, PYTHON_WORDS

DEBUG = False

BEAM_WIDTH = 100
MAX_PHRASE_LEN = 3

COMMA_INDEX = {',': 0, '-LRB-': 1, '-RRB-': 2, '.': 3, '-': 4}
SPECIAL_CHARS = {' ': '_', '(': '[LEFT_BRACKET]', ')': '[RIGHT_BRACKET]',
                 '.': '[DOT]', ',': '[COMMA]', '-': '[HYPHEN]', '\'': '[APOSTROPHE]'}
REVERSE_SPECIAL_CHARS = {v.lower(): k for k, v in SPECIAL_CHARS.items()}
REVERSE_SPECIAL_CHARS.update({v: k for k, v in SPECIAL_CHARS.items()})

CHUNK_DICT = {
    'N': ['N', 'NP', 'NN', 'NNS', 'NNP', 'NNPS'],
    'V': ['VP', 'VB', 'VBD', 'VBG', 'VBN',  'VBP', 'VBZ'],
    'P': ['PP'],
    'ADJ': ['JJ', 'JJR', 'JJS', 'ADJP'],
    'ADV': ['RB', 'RBR', 'RBS', 'ADVP'],
    'NUM': ['CD', 'QP'],
}

NER_DICT = {
    'PERSON': ['PERSON'],
    'NORP': ['NORP'],
    'ORGANIZATION': ['ORG'],
    'GPE': ['GPE'],
    'LOCATION': ['GPE', 'FACILITY', 'ORG', 'LOCATION'],
    'DATE': ['DATE'],
    'TIME': ['DATE', 'TIME'],
    'NUMBER': ['PERCENT', 'QUANTITY', 'ORDINAL', 'CARDINAL', 'MONEY'],
    'PERCENT': ['PERCENT'],
    'MONEY': ['MONEY'],
    'ORDINAL': ['ORDINAL']
}

VAR_NAMES = ['X', 'Y', 'Z', 'Answer']

nlp = English()
tokenizer = Tokenizer(nlp.vocab)

logger = logging.getLogger(__name__)

POS_TAGGER = stanza.Pipeline(lang='en', processors='tokenize,pos', tokenize_pretokenized=True)

def get_wordnet_pos(treebank_tag):
    '''Convert from Treebank POS tags to Wordnet POS tags'''
    if treebank_tag.startswith('J'):
        return wordnet.ADJ
    elif treebank_tag.startswith('V'):
        # to handle multiple verbs in a sentence
        # if treebank_tag == 'VB':
        #     return wordnet.VERB
        # else:
        #     return wordnet.NOUN
        return wordnet.VERB
    elif treebank_tag.startswith('N'):
        return wordnet.NOUN
    elif treebank_tag.startswith('R'):
        return wordnet.ADV
    else:
        return wordnet.NOUN


def fill_whitespace_in_quote(sentence):
    """input: a string containing multiple sentences;
    output: fill all whitespaces in a quotation mark into underscore"""

    def convert_special_chars(s, flag):
        return SPECIAL_CHARS[s] if s in SPECIAL_CHARS and flag else s

    flag = False  # whether space should be turned into underscore, currently
    output_sentence = ''
    for i in range(len(sentence)):
        if sentence[i] == "\"":
            flag = not flag  # flip the flag if a quote mark appears
        output_sentence += convert_special_chars(sentence[i], flag)
    return output_sentence


def preprocess_sent(sentence):
    """input: a string containing multiple sentences;
    output: a list of tokenized sentences"""
    sentence = fill_whitespace_in_quote(sentence)
    output = tokenizer(sentence)
    tokens = list(map(lambda x: x.text, output))
    ret_sentences = []
    st = 0

    # fix for ','
    new_tokens = []
    for i, token in enumerate(tokens):
        if token.endswith(','):
            new_tokens += [token.rstrip(','), ',']
        else:
            new_tokens += [token]
    tokens = new_tokens

    for i, token in enumerate(tokens):
        if token.endswith('.'):
            ret_sentences.append(tokens[st: i] + [token.strip('.')])
            st = i + 1
    return ret_sentences


def add_verb(word):
    """
    Makes the given verb a predicate and add rules for it.
    """
    predicate = "$" + word
    rules = predicate + " => S/NP {\\x. '@Action'('" + word + "', x)}\n"
    rules += predicate + " => S/PP {\\x. '@Action'('" + word + "', x)}\n"
    rules += predicate + " => (S/NP)/PP {\\y x. '@Action'('" + word + "', x, y)}\n"
    rules += predicate + " => (S/NP)/NP {\\y x. '@Action'(" + word + ", x, y)}\n"
    # rules += predicate + " => S/VP {\\x. '@Action'('" + word + "', x)}\n"
    # rules += predicate + " => (S/VP)/PP {\\y x. '@Action'('" + word + "', x, y)}\n"
    rules += predicate + " => (S/NP)/VP {\\y x. '@Action'(" + word + ", x, y)}\n"
    # rules += predicate + " => (S/VP)/NP {\\y x. '@Action'(" + word + ", x, y)}\n"
    return predicate, rules


def add_noun(word):
    """
    Makes the given noun a predicate and add rules for it.
    """
    predicate = "$" + word
    rules = predicate + " => N {'" + word + "'}\n"
    rules += predicate + " => NP {'" + word + "'}\n"
    rules += predicate + " => NP/NP {\\x. '@Concat'('" + word + "', x)}\n"
    # rules += predicate + " => NP\\NP {\\x. '@Concat'('" + word + "', x)}\n"
    rules += predicate + " => NP/VP {\\x. '@Concat'('" + word + "', x)}\n"
    rules += predicate + " => NP/PP {\\x. '@Concat'('" + word + "', x)}\n"
    rules += predicate + " => S/S {\\F. F('@Concat'('" + word + "'))}\n"
    return predicate, rules


def add_get(sentence, pos_tags):
    """
    For the sentences that don't have verbs in them,
    adds $Load at the begining of the sentence.
    """
    exists = [np.any(pos.startswith("V")) for pos in pos_tags]
    verb_to_add = ['$Load']
    if not np.any(exists):
        sentence = [verb_to_add + sentence[0]]
    return sentence


def string_to_predicate(s, pos):
    """input: one string (can contain multiple tokens with ;
    output: a list of predicates."""
    new_rules = ""
    if s != ',' and s not in REVERSE_SPECIAL_CHARS:
        s = s.lower().strip(',')
    if s.startswith("$"):
        return [s], new_rules
    elif s.startswith("\"") and s.endswith("\""):
        return ["'" + s[1:-1] + "'"], new_rules
    elif s in STRING2PREDICATE:
        if s == 'to':
            if pos == "TO":
                return ["$To_verb"], new_rules
            elif pos == "IN":
                return ["$To"], new_rules
        return STRING2PREDICATE[s], new_rules
    elif s.isdigit():
        return ["'" + s + "'"], new_rules
    elif s in WORD2NUMBER:
        return ["'" + WORD2NUMBER[s] + "'"], new_rules
    # TODO: maybe replace the allow_phrases part with a check here
    # to see if we are handling a single word or a phrase?

    # if the word is not found in our vocabulary of predicates, add it
    else:
        if pos:
            lemmatizer = WordNetLemmatizer()
            lemma_form = lemmatizer.lemmatize(s, get_wordnet_pos(pos))
            if lemma_form in STRING2PREDICATE:
                # if pos == "VBG" or pos == "VBD":
                return STRING2PREDICATE[lemma_form], new_rules
            if pos.startswith("V"):
                new_predicate, new_rules = add_verb(lemma_form)
            else:
                new_predicate, new_rules = add_noun(lemma_form)
        return [new_predicate], new_rules


def tokenize(sentence, allow_phrases=False):
    """input: a list of tokens;
    output: a list of possible tokenization of the sentence;
    each token can be mapped to multiple predicates"""
    # log[j] is a list containing temporary results using 0..(j-1) tokens
    pos_tags = [w.xpos for w in POS_TAGGER([sentence]).sentences[0].words]
    print(pos_tags)

    assert len(pos_tags) == len(sentence)
    log = {i: [] for i in range(len(sentence) + 1)}
    log[0] = [[]]
    new_lexicon = ""
    for i, (token, pos_tag) in enumerate(zip(sentence, pos_tags)):
        for _range in range(1, MAX_PHRASE_LEN + 1):
            if i + _range > len(sentence):
                break
            phrase = ' '.join(sentence[i:i + _range])
            if not allow_phrases and _range > 1:
                break
            predicates, rules = string_to_predicate(phrase, pos_tag)
            new_lexicon += rules
            for temp_result in log[i]:
                for predicate in predicates:
                    log[i + _range].append(temp_result + [predicate])
            if token.startswith("\""):  # avoid --"A" and "B"-- treated as one predicate
                break

    # adds verb if the sentence doesn't have it
    sentence = add_get(log[len(sentence)], pos_tags)
    return sentence, new_lexicon


def get_word_name(layer, st, idx):
    return "$Layer{}_St{}_{}".format(str(layer), str(st), str(idx))


def get_entry(word_name, category, semantics):
    return "\n\t\t{0} => {1} {{{2}}}".format(word_name, str(category), str(semantics))


### Helper functions for Parsing ###
def remove_punctuation(sentence):
    # TODO:
    # 1. handle dictionary/list, non-consuming
    # 2. python 2.6 -> python 26
    return sentence.translate(str.maketrans('', '', string.punctuation))


def is_number(token):
    """ Returns True is string is a number. """
    # Did it for handling not only integers, but float numbers as well.
    # The problem is that nltk parser doesn't allow '.' to be present in string
    try:
        float(token)
        return True
    except ValueError:
        return False


def quote_word_lexicon(sentence):
    """Special Handle for quoted words"""

    def is_quote_word(token):
        return (token.startswith("\'") and token.endswith("\'")) \
            or (token.startswith("\"") and token.endswith("\""))

    ret = ""
    for token in sentence:
        if is_quote_word(token):
            if token[1:-1].isdigit():
                ret += get_entry(token, 'NP', token)
                ret += get_entry(token, 'N', token)
                ret += get_entry(token, 'NP/NP',
                                 "\\x.'@Num'({},x)".format(token))
                ret += get_entry(token, 'N/N',
                                 "\\x.'@Num'({},x)".format(token))

    return ret


def remove_question_words(sentence):
    """input: a list of tokens in the query;
    output: if the query is posed as a question, removes the question tokens, as defined in QUESTION_WORDS;
    returns the list of remaining tokens
    """
    is_prefix = [np.all(sentence[:len(q_word)] == q_word)
                 for q_word in QUESTION_WORDS]
    if np.any(is_prefix):
        prefix = QUESTION_WORDS[np.where(is_prefix)[0][0]]
        sentence = sentence[len(prefix):]
    return sentence


def remove_in_python(sentence):
    """
    input: a list of tokens in the query;
    output: if the query has python with a reposition, removes the tokens, as defined in PYTHON_WORDS;
            returns the list of remaining tokens
    """
    all_sequences = [sentence[i: i + 2] for i in range(len(sentence))]
    exists = [np.any(word in all_sequences) for word in PYTHON_WORDS]

    if np.any(exists):
        word = PYTHON_WORDS[np.where(exists)[0][0]]
        index = all_sequences.index(word)
        if index + 2 >= len(sentence):
            sentence = sentence[:index]
        else:
            # for numerical values that come after python
            if sentence[index + 2].isnumeric():
                sentence = sentence[:index + 1] + sentence[index + 2:]
            sentence = sentence[:index] + sentence[index + 2:]

    return sentence


def remove_specific_word(sentence, word='python'):
    return list(filter((word).__ne__, sentence))


def getCCGParse(lwidth, tree):
    from nltk.tree import Tree
    rwidth = lwidth

    # Is a leaf (word).
    # Increment the span by the space occupied by the leaf.
    if not isinstance(tree, Tree):
        return 2 + lwidth + len(tree)

    # Find the width of the current derivation step
    for child in tree:
        rwidth = max(rwidth, getCCGParse(rwidth, child))

    # Is a leaf node.
    # Don't print anything, but account for the space occupied.
    if not isinstance(tree.label(), tuple):
        return max(
            rwidth, 2 + lwidth +
                    len("%s" % tree.label()), 2 + lwidth + len(tree[0])
        )
    (token, op) = tree.label()
    if op == "Leaf":
        return rwidth

    # Pad to the left with spaces, followed by a sequence of '-'
    # and the derivation rule.
    str_res = "%s" % (token.categ())
    if token.semantics() is not None:
        str_res += " {" + str(token.semantics()) + "}"
    if lwidth == 0:
        return str_res
    return rwidth


def parse_sentence(sentence, time_limit=10):
    """ sentence: preprocess and parse a single sentence.
    time_limit: if a positive number, TimeoutError will be thrown if parsing is not finished after time_limit seconds
    returns: a single parse tree
    """
    sentence = sentence.lower()
    split_sentence = remove_punctuation(sentence).split()
    split_sentence = remove_in_python(split_sentence)
    split_sentence = remove_specific_word(split_sentence)
    split_sentence = remove_question_words(split_sentence)
    ts, new_lexicon = tokenize(split_sentence)

    if DEBUG:
        print(ts)

    assert len(ts) == 1  # we are processing just one sentence
    ts = ts[0]
    beam_lexicon = copy.deepcopy(RAW_LEXICON) + \
        quote_word_lexicon(ts) + new_lexicon
    lex = lexicon.fromstring(beam_lexicon, include_semantics=True)
    parser = chart.CCGChartParser(lex, chart.DefaultRuleSet)

    def timeout(_, __):
        raise TimeoutError(
            "parsing sentence {} takes too long".format(sentence))

    try:
        signal.signal(signal.SIGALRM, handler=timeout)
        signal.alarm(time_limit)
        parse_tree = next(parser.parse(ts))
    except:
        # this should be called to avoid throwing one more exception
        signal.alarm(0)
        raise
    else:
        signal.alarm(0)
    return parse_tree


def example(sentence):
    # These work
    sentence = sentence.lower()
    sentence = remove_punctuation(sentence).split()
    sentence = remove_in_python(sentence)
    sentence = remove_specific_word(sentence)
    sentence = remove_question_words(sentence)
    ts, new_lexicon = tokenize(sentence)

    # ts = tokenize("find the list".split(' '))
    # ts = tokenize("find the index of an item in a list".split(' '))
    # ts = tokenize("find intersection of nested lists".split(' '))
    # ts = tokenize("round 123 to 100 instead of 100.0.split(' ')) # nltk.sem.logic.LogicalExpressionException: Unexpected token: '.' 100.0'
    # ts = tokenize("find current dir and files dir".split(' ')) # AssertionError: `'@And'(\x.'@Concat'('files',x),\x.'@Concat'('dir',x))` must be a lambda expression
    # ts = tokenize("split and parse a string in Python?"..split(' ')) # AssertionError: `'@And'(\x y.'@Split'(x,y),\y x.'@Parse'('@Desc'(x),y))` must be a lambda expression
    # ts = tokenize("find all files in a dir with extension .txt".split(' ')) # nltk.sem.logic.LogicalExpressionException: Unexpected token: '.'. in '.txt'
    # ts = tokenize("use glob to find files recursively".split(' '))
    # ts = tokenize("find the duplicates in a list and create another list with them".split(' '))

    beam_lexicon = copy.deepcopy(RAW_LEXICON) + \
        quote_word_lexicon(ts[0]) + new_lexicon
    lex = lexicon.fromstring(beam_lexicon, include_semantics=True)
    parser = chart.CCGChartParser(lex, chart.DefaultRuleSet)
    for tsi in ts:
        print(tsi)
        for parse in parser.parse(tsi):
            chart.printCCGDerivation(parse)
            # just print the first one
            break
        break


if __name__ == "__main__":
    # First time running will require downloading following nltk datasets
    # nltk.download('wordnet')
    # nltk.download('averaged_perceptron_tagger')
    # stanza.download('en')
    import time
    s = time.time()
    # chart.printCCGDerivation(parse_sentence('how to find the index of a value in 2d array in python?'))
    parse_sentence("sorting a dictionary by a key")
    print("elapsed: ", time.time() - s)
