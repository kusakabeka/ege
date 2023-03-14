from itertools import *
def u(x, y, z, w): return ((x <= w) and (not(y) <= z)) <= ((z == x) or (w and not(y)))
print(*{p for p in permutations('xyzw')
for a, b, c, d, e in product(*[[0, 1]] * 5)
if 3 == sum(u(**dict(zip(p, r))) == 0 for r in {(0, a, 0, 0), (b, 1, 1, 1), (c, d, e, 0)})})
