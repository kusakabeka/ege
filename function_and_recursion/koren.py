import sys


def f(n):
    if n < 10:
        return n
    return f(n % 10 + n // 10)


sys.setrecursionlimit(3000)
n = int(input())
print(f(n))
