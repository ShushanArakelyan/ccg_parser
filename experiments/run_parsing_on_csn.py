import pandas as pd
from pathlib import Path
pd.set_option('max_colwidth',300)
from nltk.ccg import chart
from tqdm import tqdm
from parser import parse_sentence
import sys
import os

# df = pd.read_json('/Users/shushan/Documents/CodeSearchNet/resources/data/python/python/final/jsonl/train/python_train_0.jsonl.gz', lines=True)

# We don't yet have a custom function for printing resulting logic forms, hence redirecting stdout to file for now
sys.stdout = open('parsed_queries.txt', 'w')

csn = pd.read_json('~/CodeSearchNet/resources/data/python/final/jsonl/train/python_train_0.jsonl.gz', lines=True)
all_q_count = 0
parsed_q_count = 0

time_limit = 100

with open('failed_queries.txt', 'w') as f_out, \
        open('exceptions.txt', 'w') as ex_out, \
        open('timeout.txt', 'w') as t_out:
    data_gen = tqdm(enumerate(csn['docstring_tokens']))
    for i, q in data_gen:
        all_q_count += 1
        q = " ".join(q)
        q = q.lower()
        try:
            parse_tree = parse_sentence(q, time_limit=time_limit)
            print('*' * 120)
            print('{}: {}'.format(i, q))
            chart.printCCGDerivation(parse_tree)
            print('\n\n\n')
            parsed_q_count += 1
            sys.stdout.flush()
        except StopIteration:
            f_out.write("{} {} \n".format(q, i))
            f_out.flush()
        except TimeoutError:
            t_out.write("{} {} \n".format(q, i))
            t_out.flush()
        except Exception as ex:
            ex_out.write("{} {} \n".format(q, i))
            ex_out.write(str(ex))
            ex_out.flush()
        data_gen.set_description("success rate: {:.2f}".format(float(parsed_q_count)/all_q_count), refresh=True)
sys.stdout.close()


