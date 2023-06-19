from itertools import *

def f(x, y, z, w): return (x or (not y)) and z and (not w)
for p1, p2, p3, p4 in product([0, 1], repeat=4):
    t = [(1, 1, p1, p2),
         (p3, 1, 0, 0),
         (1, p4, 1, 0)]
    if len(t) == len(set(t)):
        for p in permutations("xyzw"):
            if [f(**dict(zip(p, r))) for r in t] == [1, 1, 1]:
                print(*p, sep="")