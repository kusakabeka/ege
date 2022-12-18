def f(x, y, c):
    if x > y:
        return 0
    if x == y:
        return 1
    if c >= 2:
        return f(x + 1, y, c)
    else:
        return f(x + 1, y, c) + f(x * 2, y, c + 1)


print(f(1, 11, 0))