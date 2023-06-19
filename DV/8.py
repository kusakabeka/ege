from itertools import *
c = 0

for i in product("АГМНСТУ", repeat=6):
    s = "".join(i)
    c += 1
    if s[0] != "У" and s.count("М") == 2 and s.count("Г") <= 1:
        print(f"{c}: {s}")
    