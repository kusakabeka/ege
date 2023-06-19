from itertools import *
c = 0
for i in product("АКМСУ", repeat=5):
    s = "".join(i)
    c += 1
    if s[0] == "К" and s[1] == "У":
        print(f"{c} -> {s}")