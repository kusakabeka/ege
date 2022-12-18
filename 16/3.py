import sys

sys.setrecursionlimit(30000)
def f(n):
    if n == 1:
        return 1
    elif n > 1:
        return 2 * f(n - 1) + g(n - 1) - 2 * n


def g(n):
    if n == 1:
        return 1
    elif n > 1:
        return f(n - 1) + 2 * g(n - 1) + n


print(f(14) + g(14))
