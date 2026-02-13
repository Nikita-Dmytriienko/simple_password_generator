import argparse
import secrets
import string


parser = argparse.ArgumentParser(description="Password Generator CLI",
epilog="Examples:\n"
            "  python passgen.py \n"
            "  python passgen.py -l 20 \n"
            "  python passgen.py -l 16 --no-digits \n"
            "  python passgen.py -l 8 --no-special \n"
            "  python passgen.py -c 5 \n"
            "  python passgen.py -l 16 -c 3 \n",
    formatter_class=argparse.RawDescriptionHelpFormatter
)

parser.add_argument(
    "-l",
    "--length",
    default=12,
    type=int,
    help="Password length is 12 by default",
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

characters = string.ascii_letters

# VALIDATION
if not args.no_digits and not args.no_digits_and_special:
    characters += string.digits

    if not args.no_special and not args.no_digits_and_special:
        characters += string.punctuation


if len(characters) == 0:
    parser.error("Empty")

if args.length <= 4:
    parser.error("Too short length for password")

for i in range(args.count):
        password = ''.join(secrets.choice(characters) for _ in range(args.length))

        if args.verbosity == 0:
            print(f"\nYour password#{i+1}:\n{password} -> {args.length} length")

        elif args.verbosity == 1:
            print(f"Your password#{i}:{password}")

         # elif args.verbosity >= 2:
         #     if args.
         #
         #
         # elif args.verbosity >= 3:
         #
         #
        print()
