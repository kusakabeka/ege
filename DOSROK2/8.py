from itertools import *

l = ["".join(i) for i in product("АКЛМНЯ", repeat=5)]
for i in range(len(l)):
    if l[i][0] == "К" and l[i][1] == "М":
        print(l[i], i + 1)