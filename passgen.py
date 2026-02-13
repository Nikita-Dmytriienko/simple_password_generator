import argparse
import random
import string


parser = argparse.ArgumentParser()
parser.add_argument("square",
                    help="display a square of a given number",
                    type=int)

parser.add_argument("-v","--verbosity",
                    help="increase output verbosity",
                    type=int,choices=[0,1,2])
args = parser.parse_args()
answer = args.square**2
if args.verbosity == 2:
    print(f"the square of {args.square} equals {answer}")
elif args.verbosity == 1:
    print(f"{args.square}^2 == {answer}")
else:
    print(answer)


def create_password():
    pass