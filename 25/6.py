from fnmatch import *

for x in range(0, 10 ** 9, 2079):
    if fnmatch(str(x), "33*21?7"):
        print(x, x // 2079)
