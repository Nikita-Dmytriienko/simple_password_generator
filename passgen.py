import argparse
import secrets
import string

ALL_LETTERS = string.ascii_letters
DIGITS = string.digits
SPECIAL = string.punctuation

FULL_POOL = ALL_LETTERS + DIGITS + SPECIAL
LETTERS_ONLY = ALL_LETTERS
LETTERS_DIGITS = ALL_LETTERS + DIGITS
LETTERS_SPECIAL = ALL_LETTERS + SPECIAL



parser = argparse.ArgumentParser(description="Password Generator CLI")

parser.add_argument(
    "-l",
    "--length",
    default=12,
    type=int,
    help="Password length is 12 by default",
    epilog="Examples:\n"
    "python passgen.py\n"
    "  python passgen.py -l 20\n"
    "  python passgen.py -l 16 --no-digits\n"
    "  python passgen.py -c 5 -l 12 --no-special\n",
    formatter_class=argparse.RawDescriptionHelpFormatter
)
parser.add_argument(
      "-c",
                    "--count",
                    default=1,
                    type=int
)
parser.add_argument(
    "-v",
    "--verbosity",
    help="increase output verbosity",
    action="count",
    default=0
)

# MUTUAL GROUP
group = parser.add_mutually_exclusive_group()

group.add_argument("--no-digits", action="store_true")
group.add_argument("--no-special", action="store_true")
group.add_argument("--no-digits-and-special", action="store_true")

args = parser.parse_args()

# VALIDATION
if args.no_digits_and_special:
        pool = LETTERS_ONLY
    elif args.no_digits:
        pool = LETTERS_SPECIAL
    elif args.no_special:
        pool = LETTERS_DIGITS
    else:
        pool = FULL_POOL


if len(pool) == 0:
    parser.error("Empty")

if args.length <= 4:
    parser.error("Too short length for password")

for i in range(args.count):
        password = ''.join(secrets.choice(pool) for _ in range(args.length))

        if args.verbosity == 0:
            print(f"Your password#{i} is {password}")

        elif args.verbosity == 1:
            print(f"Your password#{i} is {password}")

         # elif args.verbosity >= 2:
         #     if args.
         #
         #
         # elif args.verbosity >= 3:
         #
         #
         # elif args.verbosity == 4:
         #
         #
         # else: # args.verbosity == 5

        print()
