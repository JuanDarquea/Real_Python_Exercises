# test1.py
import sys
import hashlib

data = sys.stdin.read()  # reads everything from standard input
hash = hashlib.sha1(data.encode('utf-8')).hexdigest()
print(hash)