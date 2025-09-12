# reverse_exec.py
# reverse.py improved to handle and guide through 0 argument error
import sys

try:
    arg = sys.argv[1]
except IndexError:
    raise SystemExit(f"Usage: py {sys.argv[0]} <string_to_reverse>")
print(arg[::-1])