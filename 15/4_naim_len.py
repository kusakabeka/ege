p1, p2, q1, q2 = 18, 52, 16, 41
B = [i / 10 for i in range(p1 * 10, p2 * 10 + 1)]
C = [i / 10 for i in range(q1 * 10, q2 * 10 + 1)]

def f(x, A):
    return ((x in B) <= (x in A)) and ((x not in C) or (x in A))

A = set()
for x in [i / 10 for i in range(0 * 10, 60 * 10)]:
    if not f(x, A):
        A.add(x)
print(sorted(A))  # 52 - 16 = 36
