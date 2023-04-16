def f(x, y):
    if x > y or x == 11:
        return 0
    elif x == y:
        return 1
    else:
        return f(x + 1, y) + f(x * 2, y) + f(x * 3, y)
print(f(2, 15) * f(15, 25))