from functools import lru_cache

@lru_cache()
def f(n):
    if n <= 3:
        return n
    elif n % 2 == 0:
        return 2 * n + f(n - 1)
    elif n % 2 != 0:
        return n * n + f(n - 2)
c = 0
for n in range(1, 101):
    if f(n) % 3 == 0:
        c += 1

print(c)