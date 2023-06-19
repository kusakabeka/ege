import sys
from functools import *

sys.setrecursionlimit(4000)
lru_cache(None)
def f(n):
    if n < 11:
        return n    
    return n + f(n - 1)
print(f(2024) - f(2021))