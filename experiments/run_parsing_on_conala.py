import argparse
import os.path
import sys

import pandas as pd
from nltk.ccg import chart
from tqdm import tqdm
from nltk.ccg import chart

from ccg_parser.parser import parse_sentence


def parse_conala(args):
    # We don't yet have a custom function for printing resulting logic forms, hence redirecting stdout to file for now
    sys.stdout = open(args.outdir + '/parsed_queries.txt', 'w')

    if os.path.splitext(args.data)[1] == '.jsonl':
        lines = True
    else:
        lines = False
    conala = pd.read_json(args.data, lines=lines)
    all_q_count = 0
    parsed_q_count = 0

    if args.time_limit:
        time_limit = args.time_limit
    else:
        time_limit = 5

    with open(args.outdir + '/failed_queries.txt', 'w') as f_out, \
            open(args.outdir + '/exceptions.txt', 'w') as ex_out, \
            open(args.outdir + '/timeout.txt', 'w') as t_out:
        if args.n:
            data_gen = tqdm(enumerate(conala['intent'][:args.n]))
        else:
            data_gen = tqdm(enumerate(conala['intent']))
        for i, q in data_gen:
            all_q_count += 1
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


if __name__ == "__main__":
    parser = argparse.ArgumentParser()
    parser.add_argument("-data", dest="data", type=str, help="Location of the dataset", required=True)
    parser.add_argument("-outdir", dest="outdir", type=str, help="Directory to create output files", required=True)
    parser.add_argument("-time_limit", dest="time_limit", type=int, help="Timeout for parsing")
    parser.add_argument("-n", dest="n", type=int, help="Number of examples to parse")
    args = parser.parse_args()

    parse_conala(args)
