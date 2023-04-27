from itertools import *
f = open("1_a.txt")
n = int(f.readline())
a = [int(x) for x in f]
k26 = k13 = k2 = k = 0
for i in range(n):
    if a[i] % 26  == 0: k26 += 1
    elif a[i] % 13 == 0: k13 += 1
    elif a[i] % 2 == 0: k2 += 1
    else: k += 1
print(k26*(k26 - 1) // 2 + k26*(n - k26) + k2 * k13)
