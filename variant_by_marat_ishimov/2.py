from itertools import *


def f(x, y, z, w): return (not y) and (x <= ((not z) == w)) or z


for p1, p2, p3, p4 in product([0, 1], repeat=4):
    table = (
        (0, p1, 0, 0),
        (p2, 0, 1, 0),
        (p3, 0, 0, p4))
    if len(table) == len(set(table)):
        for p in permutations("xyzw"):
            if [f(**dict(zip(p, r))) for r in table] == [0, 0, 0]:
                print(*p, sep="")
