__author__ = 'Eric T Dawson'

import argparse
import sys
from LaunChair import LaunChair

def parse_args():
    parser = argparse.ArgumentParser()
    parser.add_argument("-i", "-infile", dest="infile", type=str,required=True, default=sys.stdin)
    parser.add_argument("-c", "-cores", dest="cores", type=int, default=1, required=False)
    parser.add_argument("-n", "-ncpus", dest="ncpus", type = int, default=0, required=False)
    return parser.parse_args()


if __name__ == "__main__":
    args = parse_args()
    l = LaunChair()
    l.set_file(args.infile)
    l.set_n_cpus(args.ncpus)
    l.run(args.cores)

