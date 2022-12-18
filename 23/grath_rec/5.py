def f(x, y):
    if x > y:
        return 1
    if x == y:
        return 0
    return f(x + 1, y) + f(x + 3, y)

print(f(3, 15) * f(15, 20)) #  по формуле
# типо, если из A -> B (4 дороги), а из B -> C (2 дороги), то из A -> C = 8 дорог(4 * 2)