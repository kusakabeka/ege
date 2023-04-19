from fnmatch import *
for x in range(0, 10 ** 9, 8):
    if fnmatch(str(x), "1234557*6"):
        print(x, x // 8)