def f(n):
    if n > 0:
        f(n // 3)
        print(n, end="")
        f(n - 3)


f(9)