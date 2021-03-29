from spacy.lang.en import English
from spacy.tokenizer import Tokenizer

import copy
import logging
from parser_dict import STRING2PREDICATE, WORD2NUMBER, RAW_LEXICON
from nltk.ccg import chart, lexicon


BEAM_WIDTH = 100
MAX_PHRASE_LEN = 4

COMMA_INDEX = {',': 0, '-LRB-': 1, '-RRB-': 2, '.': 3, '-': 4}
SPECIAL_CHARS = {' ': '_', '(': '[LEFT_BRACKET]', ')': '[RIGHT_BRACKET]', '.': '[DOT]', ',': '[COMMA]', '-': '[HYPHEN]', '\'': '[APOSTROPHE]'}
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

TAGS_OF_INTEREST = ['NP', 'VP', 'PP',
                    'NN', 'NNS', 'NNP', 'NNPS', 'PRP', 'PRP$',
                    'VB', 'VBD', 'VBG', 'VBN', 'VBP', 'VBZ']


nlp = English()
tokenizer = Tokenizer(nlp.vocab)

logger = logging.getLogger(__name__)

### Helper functions for Preprocessing Explanations ###

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


def string_to_predicate(s):
    """input: one string (can contain multiple tokens with ;
    output: a list of predicates."""
    if s != ',' and s not in REVERSE_SPECIAL_CHARS:
        s = s.lower().strip(',')
    if s.startswith("$"):
        return [s]
    elif s.startswith("\"") and s.endswith("\""):
        return ["'" + s[1:-1] + "'"]
    elif s in STRING2PREDICATE:
        return STRING2PREDICATE[s]
    elif s.isdigit():
        # return ["'" + s + "'"]
        return ["$UNK"]
    elif s in WORD2NUMBER:
        # return ["$UNK"]
        return ["'" + WORD2NUMBER[s] + "'"]
    # TODO: maybe replace the allow_phrases part with a check here
    # to see if we are handling a single word or a phrase?

    # if the word is not found in our vocabulary of predicates, add it
    else:
        global RAW_LEXICON
        new_predicate = "$" + s
        new_rules = new_predicate + "  => NP {'" + s + "'}\n"
        new_rules += new_predicate + " => NP/NP {\\x. '@Concat'('" + s  +"', x)}\n"
        RAW_LEXICON += new_rules
        return [new_predicate]


def tokenize(sentence, allow_phrases=False):
    """input: a list of tokens;
    output: a list of possible tokenization of the sentence;
    each token can be mapped to multiple predicates"""
    # log[j] is a list containing temporary results using 0..(j-1) tokens
    log = {i: [] for i in range(len(sentence) + 1)}
    log[0] = [[]]
    for i, token in enumerate(sentence):
        for _range in range(1, MAX_PHRASE_LEN + 1):
            if i + _range > len(sentence):
                break
            phrase = ' '.join(sentence[i:i + _range])
            if not allow_phrases and _range > 1:
                break
            predicates = string_to_predicate(phrase)
            for temp_result in log[i]:
                for predicate in predicates:
                    log[i + _range].append(temp_result + [predicate])
            if token.startswith("\""):  # avoid --"A" and "B"-- treated as one predicate
                break
    return log[len(sentence)]


def get_word_name(layer, st, idx):
    return "$Layer{}_St{}_{}".format(str(layer), str(st), str(idx))


def get_entry(word_name, category, semantics):
    return "\n\t\t{0} => {1} {{{2}}}".format(word_name, str(category), str(semantics))


### Helper functions for Parsing ###

def quote_word_lexicon(sentence):
    """Special Handle for quoted words"""

    def is_quote_word(token):
        return (token.startswith("\'") and token.endswith("\'")) \
            or (token.startswith("\"") and token.endswith("\""))

    ret = ""
    for token in sentence:
        if is_quote_word(token):
            ret += get_entry(token, 'NP', token)
            ret += get_entry(token, 'N', token)
            ret += get_entry(token, 'NP', "'@In'({},'all')".format(token))
            if token[1:-1].isdigit():
                ret += get_entry(token, 'NP/NP', "\\x.'@Num'({},x)".format(token))
                ret += get_entry(token, 'N/N', "\\x.'@Num'({},x)".format(token))
                ret += get_entry(token, 'PP/PP/NP/NP', "\\x y F.'@WordCount'('@Num'({},x),y,F)".format(token))
                ret += get_entry(token, 'PP/PP/N/N', "\\x y F.'@WordCount'('@Num'({},x),y,F)".format(token))

    return ret


def example():
    # These work
    ts = tokenize("split string every nth character".split(' '))
    # ts = tokenize("find the list".split(' '))

    # These do not work
    # a) how to turn number tokens into something in logic form?
    # ts = tokenize("find two lists".split(' '))
    # desired output after parsing: "@Find('List', '2')" or "@Find('List', '2 lists')"
    # b) how to handle out of vocabulary expressions, we want to pass
    # them as a textual argument, e.g.
    # ts = tokenize("find jibberjabber gobbledygook lists".split(' '))
    # desired output after parsing: @Find('List', 'jibber-jabber gobbledygook lists')

    # Example: "Finding the index of an item in a list"
    # Example: "Find intersection of two nested lists?"
    # 1) *.lowercase()
    # 1a) remove question words and question marks at the end
    #TODO: 2) bring verbs to their canonical form: finding -> find
    #"find the index of an item in a list" -> @Find(what = "the index of an item"[NP], where="in a list"[PP?])
    #"find intersection of two nested lists" -> @Find(what = "intersection of two nested lists"[NP])

    # ts = tokenize("find the index of an item in a list".split(' '))
    # ts = tokenize("find intersection of nested lists".split(' '))
    # ts = tokenize("find current dir and files dir".split(' ')) # AssertionError: `'@And'(\x.'@Concat'('files',x),\x.'@Concat'('dir',x))` must be a lambda expression
    # ts = tokenize("find all files in a dir with extension .txt".split(' ')) # nltk.sem.logic.LogicalExpressionException: Unexpected token: '.'. in '.txt'
    # ts = tokenize("use glob to find files recursively".split(' '))
    # ts = tokenize("find the duplicates in a list and create another list with them".split(' '))
    lex = lexicon.fromstring(RAW_LEXICON, include_semantics=True)
    parser = chart.CCGChartParser(lex, chart.DefaultRuleSet)
    for tsi in ts:
        print(tsi)
        for parse in parser.parse(tsi):
            chart.printCCGDerivation(parse)
            # just print the first one
            break
        break

if __name__ == "__main__":
    example()