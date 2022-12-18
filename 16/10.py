from functools import lru_cache


@lru_cache()
def f(n):
    if n <= 3:
        return n
    elif n % 2 == 0:
        return 2 * n * n + f(n - 1)
    elif n % 2 != 0:
        return n * n * n + n + f(n - 1)


c = 0
for n in range(1, 100):
    if f(n) < 10 ** 7:
        c += 1

print(c)
