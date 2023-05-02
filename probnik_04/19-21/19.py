def f(a, b, c, m):
    if a + b >= 52: return c % 2 == m % 2
    if c == m: return 0
    # + 2(префиксные  суммы и последовательности) -- *3
    h = [f(a + 2, b, c + 1, m),
         f(a, b + 2, c + 1, m),
         f(a * 3, b, c + 1, m),
         f(a, b * 3, c + 1, m)]
    return any(h) if (c + 1) % 2 == m % 2 else all(h)

for b in range(1, 47):
    for m in range(1, 5):
        if f(5, b, 0, m) == 1:
            if m == 4: print(b, m)
            break
# 19 - 6
# 20 - 5,6
# 21 -