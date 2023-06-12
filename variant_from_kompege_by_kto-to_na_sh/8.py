from itertools import *
c = 0
for i in product("ЛМСЫЬ", repeat=5):
    s = "".join(i)
    c += 1
    if s[0] == "Ы" and s[1] == "Ы":
        print(f"{c}: {s}")
