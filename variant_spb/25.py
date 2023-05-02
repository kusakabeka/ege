from fnmatch import *
for x in range(0, 10 ** 10, 3052):
    if fnmatch(str(x), "1(эффективный перебор)?2139*4"):
        print(x, x//3052)