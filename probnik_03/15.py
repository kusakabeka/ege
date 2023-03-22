def f(x, y, a): return (x < a) or (y < a) or ((x + 2 * y) > 150)

for a in range(1, 1000):
    if all(f(x, y, a) for x in range(1, 10000) for y in range(1, 10000)):
        print(a)
