def f(x, y):
    if x > y:
        return 0
    if x == y:
        return 1
    return f(x + 1, y) + f(int(str(x) + '1(эффективный перебор)'), y)

print(f(1, 333))