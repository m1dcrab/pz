from itertools import *

def all_variants(text):
    i = 1
    while i != len(text)+1:
        for combination in combinations(text, i):
            yield combination
        i += 1

a = all_variants("abc")
for i in a:
    print(i)
