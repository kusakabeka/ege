from itertools import *

def f(x, y, z, w): return (x and (not y))

for p1, p2, p3, p4 in product([0, 1], repeat=4):
    t = [(), 
         (), 
         ()]
    if len(t) == len(set(t)):
        for p in permutations("wxyz"):
            if [f(**dict(zip(p, r))) for r in t] == [1, 1, 1]:
                print(*p, sep="")
                