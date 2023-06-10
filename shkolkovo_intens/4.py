from itertools import *
c = 0
for s in product("МАШИНА", repeat=6):
    if ([s[0], s[2], s[4]] == sorted([s[0], s[2], s[4]])) and ([s[1], s[3], s[5]] == sorted([s[1], s[3], s[5]])):
        c += 1
print(c)