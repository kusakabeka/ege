from itertools import *

def f(x, y, z, w): return z or (not(w <= x)) or ((not z) <= (not y))



for p1, p2, p3, p4, p5, p6 in product([0, 1], repeat = 6):
    t = ([p1, 0, 1, 1],
         [1, p2, 1, p3],
         [p4, p5, p6, 1])
    if len(t) == len(set(t)):
        for p in permutations("xyzw"):
            if [f(**dict(zip(p, r))) for r in t] == [0,0,0]:
                    print(p, sep="")
