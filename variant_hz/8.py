from itertools import *
c = 0
for i in product("012345678", repeat=7):
    s = "".join(i)
    if s.count("8") == 1 and s[0] != "0" and s[0] not in "1357" and s[-1] not in "02468":
        c += 1

print(c)
