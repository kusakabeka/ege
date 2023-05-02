from fnmatch import *

for i in range(273, 10 ** 8, 273):
    if fnmatch(str(i), "12??36*1(эффективный перебор)"):
        print(i, i // 273)