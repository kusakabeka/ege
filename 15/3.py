p1, p2, p3, p4, p5, p6, p7, p8, p9, p10, q1, q2, q3, q4, q5, q6, q7, q8, q9, q10 = 2, 4, 6, 8, 10, 12, 14, 16, 18, 20, 5, 10, 15, 20, 25, 30, 35, 40, 45, 50
P = [i / 10 for i in range(p1 * 10, p10 * 10 + 1)]
Q = [i / 10 for i in range(q1 * 10, q10 * 10 + 1)]

def f(x, A):
    return ((x in A) <= (x in P)) and ((x in Q) <= (x not in A))
A = set([i / 10 for i in range(0 * 10, 60 * 10)])
for x in [i / 10 for i in range(0 * 10, 60 * 10)]:
    if not f(x, A):
        A.remove(x)
print(sorted(A))
