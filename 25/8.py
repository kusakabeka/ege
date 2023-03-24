from fnmatch import *

for x in range(0, 10 ** 8, 149):
    if fnmatch(str(x), "1?234*6"):
        print(x, x // 149)
