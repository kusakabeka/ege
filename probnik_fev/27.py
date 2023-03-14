f = open("27A.txt")
n = int(f.readline())
a = [int(x) for x in f]
mx = 0
for i in range(n):
    k0 = k1 = 0
    for j in range(i, n):
        if a[j] % 2 == 0: k0 += 1
        else: k1 += 1
        if k0 == k1:
            mx = max(mx, k0+k1)
print(mx)