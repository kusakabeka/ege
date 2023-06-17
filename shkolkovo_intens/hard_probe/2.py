from itertools import *

def f(x,y,z,w): return (x or (not y)) == ((not w) <= (z == (bool((not x)) ^ bool(y))))

for p1, p2, p3, p4, p5 in product([0, 1], repeat = 5):
    t = [(p1, p2, p3, 1),
         (1, p4, 0, 1),
         (0, 1, 1, 0),
         (1, p5, 1, 1)]
    if len(t) == len(set(t)):
        for p in permutations("xyzw"):
            if [f(**dict(zip(p, r))) for r in t] == [0, 0, 0, 0]:
                print(*p, sep="")
'''
ans = wxzy
'''
