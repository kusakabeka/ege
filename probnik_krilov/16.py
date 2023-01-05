from functools import lru_cache


@lru_cache()
def f(n):
    if n < 3:
        return 1
    if n > 2 and n % 2 != 0:
        return f(n - 1) - f(n - 2)
    if n > 2 and n % 2 == 0:
        summ = 0
        for i in range(1, n):
            summ += f(i)
        return summ


print(f(39))  # 41518080
