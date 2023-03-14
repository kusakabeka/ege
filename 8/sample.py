from itertools import *
#10154
c = 0
for x in product("0123456", repeat=5):
    s = "".join(x)
    if s[0] != "0" and s.count("6") == 1:
        ch = sum(int(x) for x in s if int(x) % 2 == 0)
        nch = sum(int(x) for x in s if int(x) % 2 != 0)
        if ch < nch:
            c += 1
print(c)