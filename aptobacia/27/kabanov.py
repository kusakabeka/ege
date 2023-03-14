f = open("27A.txt")
n = int(f.readline())
a = []
for i in range(n):
    km, k = map(int, f.readline().split())
    c = k // 48 if k % 48 == 0 else k // 48 + 1
    a.append([km, c])
m = 10 ** 20
for i in range(n):
    c = 0
    for j in range(n):
        r = abs(a[i][0] - a[j][0])
        c += r * a[j][1]
    m = min(m, c)
print(m)
