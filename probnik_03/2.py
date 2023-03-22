from itertools import *


def f(x, y, w, z):
    return not(z or (w <= y)) or (x <= z)


for a1, a2, a3, a4, a5, a7, a6 in product([0, 1], repeat=7):
    t = ((0, a1, 0, a2),(a3, 0, 1, a4),(a5, 1, a6, a7))
    if len(t) == len(set(t)):
        for p in permutations("xywz"):
            if [f(**dict(zip(p, r))) for r in t] == [0, 0, 0]:
                print(p)
