from fnmatch import *

for i in range(0, 10 ** 9, 2079):
    if fnmatch(str(i), '33*21?7'):
        print(i, i // 2079)