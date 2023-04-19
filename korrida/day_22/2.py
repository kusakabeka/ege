from fnmatch import *
for x in range(0, 10 ** 9, 163):
    if fnmatch(str(x), "3261??64*"):
        print(x, x // 163)