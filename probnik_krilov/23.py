def f(x, y): # 60 -> 1
    if x < y or x == 4:
        return 0
    if x == y:
        return 1
    return f(x - 1, y) + f(x // 2, y)


print(f(60, 20) * f(20, 1))

