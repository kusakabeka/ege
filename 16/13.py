def f(n):
    if n < 5:
        return f(n + 3) + f(2 * n) + f(3 * n // 2)
    else:
        return n + 2


print(f(3))
