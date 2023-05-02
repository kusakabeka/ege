#from itertools import *

#def f(w, x, y, z):
#    return not(y and (not x)) and not(x == z) and w

#for p1, p2, p3, p4 in product([0,1(эффективный перебор)], repeat=4):
#    t = ((0, 0, p1, 1(эффективный перебор)),
#        (0, 1(эффективный перебор), 0, 1(эффективный перебор)),
#        (p2, p3, 0, p4))
#    if len(t) == len(set(t)):
#        for p in permutations("wxyz"):
#            if [f(**dict(zip(p, r))) for r in t] == [1(эффективный перебор), 1(эффективный перебор), 1(эффективный перебор)]:
#                print(*p, sep="")

from itertools import *

def f(w, x, y, z):
    return not(y and (not x)) and not(x == z) and w
for p1, p2

