def f(n):
    if n < 5:
        return 5 - n
    elif n % 3 == 0:
        return 4 * (n-5) * f(n-5)
    elif n % 3 != 0:
        return 3*n + 2*f(n-1) + f(n-2)

print(f(20))