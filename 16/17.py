def f(k, n):
    k += 1
    if k % 2 == 0 and n > 0:
        f(k, n // 3)
        print(n, end="")
        f(k, n - k)
    if k % 2 == 1 and n > 0:
        f(k, n // 2)
        f(k, n - k - 1)
        print(n, end="")


f(0, 6)
