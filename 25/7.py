from fnmatch import *

for x in range(0, 10 ** 8, 129):
    if fnmatch(str(x), "12?3*46"):
        print(x, x // 129)
