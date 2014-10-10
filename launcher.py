__author__ = 'Eric T Dawson'

import argparse
import sys
from LaunChair import LaunChair

def parse_args():
    parser = argparse.ArgumentParser()
    parser.add_argument("-i", dest="infile", type=str, default=sys.stdin)
    parser.add_argument("-c", dest="cores", type=int, default=4)
    return parser.parse_args()


if __name__ == "__main__":
    args = parse_args()
    l = LaunChair()
    l.set_file(args.infile)
    l.run(args.cores)

