from fnmatch import *

for x in range(0, 10 ** 10, 2023):
    if fnmatch(str(x), "1?493*41"):
        print(x, x // 2023)
