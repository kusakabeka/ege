from fnmatch import *
for x in range(0, 10 ** 9, 137):
    if fnmatch(str(x), "1234*7?8"):
        print(x, x//137)
'''
        
12349728 90144
123408778 900794
123419738 900874
123445768 901064
123456728 901144
123471798 901254
123482758 901334
123493718 901414

'''