def f(x, y, a): return (x > a) or (y > a) or (y - 2 * x + 12 != 0)
for a in range(1, 1000):
    if all(f(x, y, a) for x in range(1, 1000) for y in range(1, 10000)): print(a)