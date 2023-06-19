def f(x, y): return (x < a) or (y < a) or (x + 2*y > 50)
for a in range(1, 10000):
    if all(f(x, y) for x in range(1, 10000) for y in range(1, 10000)) == 1:
        print(a)
