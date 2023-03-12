from itertools import *
def u(w, x, y, z): return 1 - (z <= x) or y == w or w
print(*{p for p in permutations('wxyz')
for a, b, c, d, e, f in product(*[[0, 1]] * 6)
if 3 == sum(u(**dict(zip(p, r))) == 0 for r in {(0, 0, a, b), (0, c, d, e), (0, 1, f, 0)})})
