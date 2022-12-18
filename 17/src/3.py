f = open('17-1.txt')
a = []
for x in f:
    a.append(int(x))

c = 0
min_c = 10 ** 6

for i in range(len(a) - 1):
    if (a[i] % 11 == 0 and a[i] % 13 == 0 and a[i] % 15 != 0 and a[i] % 17 != 0) or \
            (a[i + 1] % 11 == 0 and a[i + 1] % 13 == 0 and a[i + 1] % 15 != 0 and a[i + 1] % 17 != 0):
        c += 1
        min_c = min(min_c, a[i] + a[i + 1])
print(c, min_c)

f.close()
