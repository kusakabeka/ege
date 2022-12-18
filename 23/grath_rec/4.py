def f(x, y):
    if x > y:
        return 0
    if x == y:
        return 1
    if x == 8: # тк нельзя идти через восьмерку
        # то у нас 0 решений
        return 0
    return f(x + 1, y) + f(x + 2, y) + f(x + 3, y)
print(f(3, 15))