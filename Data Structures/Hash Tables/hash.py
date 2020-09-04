# Hash tables are called as dictionary in Python

basket = dict()

basket["grapes"] = 1000
print(basket)

import hashlib

print(hashlib.md5("hello".encode()).hexdigest())
print(hashlib.sha256("hello".encode()).hexdigest())
