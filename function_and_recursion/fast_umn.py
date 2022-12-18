def f(a, n):
    if n == 0:
        return 1
    elif n % 2 == 0:
        return f(a ** 2, n / 2)
    else:
        return a * f(a, n - 1)


a = int(input())
n = int(input())

print(f(a, n))