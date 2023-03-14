P = [2, 4, 6, 8, 10, 12, 14, 16, 18, 20]
Q = [3, 6, 9, 12, 15, 18, 21, 24, 27, 30]
R = [12, 24, 36, 48, 60]

def f(x, A):
    return (x not in A) <= (((x in P) and (x in Q)) <= (x in R))

A = set()
for x in range(0, 70):
    if not f(x, A):
        A.add(x)
print(sorted(A)) # 108

