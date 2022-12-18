from itertools import *
c = 1
for i in product('АОУ', repeat=5):
    s = ''.join(i)
    c += 1
    if c == 101:
        print(s)