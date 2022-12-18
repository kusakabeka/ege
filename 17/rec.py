def f(n):
    if n < 1:
        return n
    else:
        return f(n) * f(n-1)
n = int(input())
print(f(n))