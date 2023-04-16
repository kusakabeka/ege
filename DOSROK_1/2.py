from itertools import *


def f(x, y, z, w): return (x and (not y)) or (y == z) or ((not w))


for p1, p2, p3, p4 in product([0, 1], repeat=4):
    t = [(0, p1, p2, 0),
         (0, 1, 0, 1),
         (p3, 1, 0, p4)]
    if len(t) == len(set(t)):
        for p in permutations("xyzw"):
            if [f(**dict(zip(p, r))) for r in t] == [0, 0, 0]:
                print(*p, sep="")
'''
2000 - 1545
'''