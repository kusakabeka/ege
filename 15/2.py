p1, p2, q1, q2 = 12, 26, 30, 53
P = [i / 10 for i in range(p1 * 10, p2 * 10 +1 )]
Q = [i / 10 for i in range(q1 * 10, q2 * 10 +1 )]

def f(x, A):
    return ((x in A) <= (x in P)) or (x in Q)
A = set([i / 10 for i in range(0 * 10, 60 * 10)])
for x in [i / 10 for i in range(0 * 10, 60 * 10)]:
    if not f(x, A):
        A.remove(x)
print(sorted(A)) # [12;26] and [30;53] -- 23