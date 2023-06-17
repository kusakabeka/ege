from itertools import *

def f(w, z, x, y): return (z and w <= y) and (x or y or w)

found_solution = False

for p1, p2, p3, p4, p5, p6 in product([0, 1], repeat=6):
    t = [(1, 0, 0, p1),
         (p2, 1, 0, p3),
         (p4, p5, 1, p6)]
    if len(t) == len(set(t)):
        for p in permutations("wxyz"):
            if [f(**dict(zip(p, r))) for r in t] == [0, 0, 0]:
                print(*p, sep="")
                found_solution = True
                break  # Выходим из цикла после нахождения решения
        if found_solution:
            break  # Выходим из внешнего цикла после нахождения решения
