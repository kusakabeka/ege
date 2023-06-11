from functools import lru_cache

@lru_cache(None)
def f(x, y):
    if x > y: return 0
    elif x == y: return 1
    else: return f(x + 1, y) + f(x + 4, y)
print(f(1, 128))