def f(x, y):
    if x > y or x == 10 or x == 15:
        return 0
    if x == y:
        return 1
    return f(x + 1, y) + f(x + 2, y) + f(x + 3, y)


print(f(5, 11)*f(11, 18))
