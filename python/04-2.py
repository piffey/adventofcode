#!/usr/bin/env python

from hashlib import md5

with open('../inputs/04.txt') as f:
    secret_key = f.readline().strip()
suffix = 1
while not md5('{}{}'.format(secret_key, suffix)).hexdigest().startswith('000000'):
    suffix += 1
print(suffix)
