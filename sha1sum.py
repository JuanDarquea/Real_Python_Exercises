# sha1sum.py

import sys
import hashlib

data = sys.argv[1]
m = hashlib.sha1()
m1 = m.update(bytes(data, 'utf-8'))
print(data)
print(m)
print(m1)
print(m.hexdigest())