from itertools import *


def u(w, x, y, z):
    return 1 - (y <= 1 - (z <= w)) and (1 - z <= (1 - w == x))


# repeat = количеству "?"
for a, b, c, d, e, f in product([0, 1], repeat=6):
    t = ((1, a, 1, 1, 0),  # последний столбик - значение функции
         (b, c, 0, 0, 1),  # последний столбик - значение функции
         (e, 0, 0, f, 1))  # последний столбик - значение функции
    if len(t) == len(set(t)):
        for p in permutations("wxyz"):
            #если функция все время равна либо 1
            #либо 0, то  all(u(**dict(zip(p, r))) == 0
            #если функция возвращает разные значение, то
            # all(u(**dict(zip(p, r))) == r[-1]
            if all(u(**dict(zip(p, r))) == r[-1] for r in t):
                print(*p)
