def f(n):
    if n < 5:
        return f(n + 2) + f(n + 3) + f(n + 1)
    else:
        return n

print(f(2))