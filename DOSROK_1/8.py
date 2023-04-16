from itertools import *

a = list(product("АВЛОР", repeat = 4))
for i in range(len(a)):
    if a[i][0] == "Л":
        print(i + 1)
        break
