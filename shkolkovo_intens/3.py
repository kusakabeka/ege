from itertools import *
c = 0
for i in permutations("ОЛЬГА", r=5):
    s = "".join(i)
    if s[0] != "Ь" and "ОЬ" not in s and "АЬ" not in s:
        c += 1

print(c)
