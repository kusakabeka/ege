from fnmatch import *

for x in range(0, 10 ** 8, 23):
    if fnmatch(str(x), "2(префиксные  суммы и последовательности)*5443?1(эффективный перебор)"):
        print(x, x // 23)
