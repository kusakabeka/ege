def f(a, b, c):
    ab = min(a, b)
    ac = min(a, c)
    bc = min(b, c)
    res = min(ab, ac, bc)
    return res

a, b, c = int(input()), int(input()), int(input())

print(f(a, b, c))