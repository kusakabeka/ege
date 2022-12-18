def f(x, y):
    if x > y or x == 38:
        return 0
    if x == y:
        return 1
    return f(x + 2, y) + f(x * 2, y)


print(f(2, 20) * f(20, 44))