f = open("...")
n = int(f.readline())
a = [int(x) for x in f]
ms = 0
for i in range(n):
    s = 0
    for j in range(i, n):
        s += a[j]
        if s % 100:
            ms = max(ms, s)