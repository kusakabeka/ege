with open("2A.txt") as f:
    n = int(f.readline())
    a = [int(_) for _ in f]
c2, c7, c14 = 0, 0, 0
for i in range(n):
    if a[i] % 2 == 0 and a[i] % 14 != 0: c2 += 1
    elif a[i] % 7 == 0 and a[i] % 14 != 0: c2 += 1
    elif a[i] % 14 == 0: c14 += 1
print(c14 * (c14 - 1) / 2 * (n - c14) + c2 * c7)