from itertools import *

c = 0
index = 1
for n, i in enumerate(product("ЕКОФ", repeat=5), start=1):
    s = "".join(i)
    if s.count("О") == 1 and all(x not in s for x in ("КО", "ФО", "ОК", "ОФ")):
        c += 1
        print(f"{n}: {s}")


