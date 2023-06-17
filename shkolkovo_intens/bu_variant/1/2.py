from itertools import *

def f(x, y, z, w):
    pass

for p1, p2, p3, p4 in product([0,1], repeat=4):
    t = ([],
         [],
         [])
    if len(t) == len(set(t)):
        for p in permutations("wxyz"):
            