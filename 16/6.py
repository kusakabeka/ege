from functools import lru_cache

c = 0


@lru_cache()
def f(n):
    if n <= 3: return n
    if n % 2 == 0: return 2 * n * n + f(n - 1)
    if n % 2 != 0: return n * n * n + n + f(n - 1)


for n in range(1, 10 ** 10):
    if f(n) < 10 ** 7:
        c += 1
print(c)
