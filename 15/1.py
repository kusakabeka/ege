p1, p2, q1, q2 = 3, 15, 14, 25

P = [i / 10 for i in range(p1 * 10, p2 * 10 + 1)]
Q = [i / 10 for i in range(q1 * 10, q2 * 10 + 1)]

def f(x, A):
    return ((x in P) == (x in Q)) <= (x not in A)

A = set([i / 10 for i in range(0 * 10, 30 * 10)])
for x in [i / 10 for i in range(0 * 10, 30 * 10)]:
    if not f(x, A):
        A.remove(x)
print(sorted(A)) # [3, 14) and (15; 25]