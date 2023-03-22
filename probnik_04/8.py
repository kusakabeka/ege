from itertools import *
c = 0
for i in product("0123456", repeat=6):
    s = "".join(i)
    if s.count('6') == 1 and ((s[0] in "246" and s[1] in "135" and s[2] in "0246" and s[3] in "135" and s[4] in "0246" and s[5] in "135") or \
            (s[0] in "135" and s[1] in "0246" and s[2] in "135" and s[3] in "0246" and s[4] in "135" and s[5] in "0246")):
        c += 1
print(c)