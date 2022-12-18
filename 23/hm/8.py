def f(x, y):
    if x > y or x == 3 or x == 13 or x == 23 or x == 30 or x == 31 or x == 32 or x == 33 or x == 34 or x == 35 or x == 36 or x == 37 or x == 38 or x == 39:
        return 0
    if x == y:
        return 1
    return f(x + 1, y) + f(x * 2, y)

print(f(1, 40))
