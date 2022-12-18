start = 1
fin = 18
a = [0] * (fin + 1)
a[1] = 1
for i in range(start + 1, fin + 1):
    a[i] += a[i-1]
    if i - 3 >= 1:
        a[i] += a[i-3]
    if i % 4 == 0:
        a[i] += a[i // 4]

print(a[-1])










