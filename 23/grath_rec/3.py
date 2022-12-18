def f(x, y) -> int:
    if x > y:
        return 0
    if x == y:
        return 1
    return f(x + 1, y) + f(x + 3, y) + f(x * 4, y)
print(f(1, 18))