def f(x, y, c):
    if c == 10:
        return x == y
    else:
        return f(x + 4, y,c + 1) + f(x + 7, y, c + 1) + f(x // 2, y, c + 1)
print(f(1, 1, 0))