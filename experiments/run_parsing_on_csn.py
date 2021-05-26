import argparse
import os

import pandas as pd
from tqdm import tqdm

from parser import parse_sentence, get_ccg_parse, postprocess_parse


def parse_csn(args):
    csn = pd.read_json(args.data, lines=True)
    # "%%%" signifies empty parse
    parses_dict = {i: "%%%" for i in range(len(csn))}
    all_q_count = 0
    parsed_q_count = 0

    if args.time_limit:
        time_limit = args.time_limit
    else:
        time_limit = 100
    assert os.path.isdir(args.logdir)
    with open(args.logdir + '/failed_queries.txt', 'w') as f_out, \
            open(args.logdir + '/exceptions.txt', 'w') as ex_out, \
            open(args.logdir + '/timeout.txt', 'w') as t_out:
        if args.n:
            data_gen = tqdm(enumerate(csn['docstring_tokens'][:args.n]))
        else:
            data_gen = tqdm(enumerate(csn['docstring_tokens']))
        for i, q in data_gen:
            all_q_count += 1
            q = " ".join(q)
            q = q.lower()
            try:
                parse_tree = parse_sentence(q, time_limit=time_limit)
                parse_str = get_ccg_parse(parse_tree)
                parses_dict[i] = postprocess_parse(parse_str)
                parsed_q_count += 1
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
            data_gen.set_description("success rate: {:.2f}".format(float(parsed_q_count) / all_q_count), refresh=True)
    csn['parses'] = csn.index.map(parses_dict)
    csn.to_json(args.output, orient="records", lines=True)


if __name__ == "__main__":
    parser = argparse.ArgumentParser()
    parser.add_argument("-data", dest="data", type=str, help="Location of the input file, should be jsonl",
                        required=True)
    parser.add_argument("-output", dest="output", type=str, help="Name of the output file, should be jsonl",
                        required=True)
    parser.add_argument("-time_limit", dest="time_limit", type=int, help="Timeout for parsing")
    parser.add_argument("-n", dest="n", type=int, help="Number of examples to parse")
    parser.add_argument("-logdir", dest="logdir", type=int,
                        help="This directory will be used to log failed and timed out queries")
    args = parser.parse_args()

    parse_csn(args)
