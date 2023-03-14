from itertools import *
c = 0
for i in product("–”—À¿Õ", repeat=5):
    s = "".join(i)
    if (s.count("”") <= 1 and s.count("¿") <= 1) or (s.count("¿") == 0 and s.count("”") == 0) or (s.count("”") <= 1 and s.count("¿") == 0) or (s.count("”") == 0 and s.count("¿") <= 1):
        c += 1
print(c)