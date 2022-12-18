def f(x, y):
    if x < y: # тк мы идем из 30 в 1
        return 0
    if x == y:
        return 1
    return f(x - 1, y) + f(x // 2, y)
print(f(30, 8) * f(8, 1))