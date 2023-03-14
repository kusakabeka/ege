from functools import lru_cache
from sys import setrecursionlimit

setrecursionlimit(3000)


@lru_cache
def f(n):
    if n == 1: return 1
    if n > 1: return n * f(n - 1)


'''
f(2023) = (f(2022) * 2023 - f(2022)) /  
8262826164
'''
