# sha1sum_bytes.py

import os
import sys
import hashlib

data = os.fsencode(sys.argv[1])
m = hashlib.sha1()
m1 = m.update(data)
print(data)
print(m)
print(m1)
print(m.hexdigest())