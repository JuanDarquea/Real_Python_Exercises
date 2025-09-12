# args_other.py
import sys

def main(args = None):
    if args is None:
       	args = sys.argv[1:]
    print(f"Arguments of the script: {args}")
print(f"Name of the scrypt: {sys.argv[0]}")
main()