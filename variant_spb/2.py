from itertools import *


def f(x, y, w, z):
    return ((x <= w) and ((not y) <= z)) <= ((z == x) or (w and (not y)))


for a1, a2, a3, a4, a5 in product([0, 1], repeat=5):
    t = ((0, a1, 0, 0),(a2, 1, 1, 1),(a3, a4, a5, 0))
    if len(t) == len(set(t)):
        for p in permutations("xywz"):
            if [f(**dict(zip(p, r))) for r in t] == [0, 0, 0]:
                print(p)
