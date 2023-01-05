from itertools import *

c = 0
for i in product('АЗЛОПЬ', repeat=6):
    s = "".join(i)
    c += 1
    if (s.count('Ь') <= 1) and (s.count('А') == 1) and (s.count('З') <= 2):
        print(c)
        exit()