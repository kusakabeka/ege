from itertools import *


def f(w, x, y, z): return not((w or (not y)) and x) or (y == z)

for a, b, c, d in product([0, 1], repeat=4):
    t = ((0, 1, a, 0), 
         (1, 1, 0, b),
         (c, 1, d, 0))
    if len(t) == len(set(t)):
        for p in permutations("wxyz"):
            if [f(**dict(zip(p, r))) for r in t] == [0, 0, 0]:
               print(*p)
