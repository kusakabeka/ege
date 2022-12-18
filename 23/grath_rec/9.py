def f(x, y, c):
    if x < y:
        return 0
    if x == y:
        return 1
    if c > 0:
        return f(x - 2, y, 0)
    else:
        return f(x - 2, y, 0) + f(x // 2, y, 1)
print(f(50, 1, 0))