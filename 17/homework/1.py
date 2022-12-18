with open('17-1.txt') as f:
    a = list(map(int, f.readlines()))
c = 0
minn = 1000000000
summ = 0
for i in range(len(a) - 1):
    if (a[i] % 11 == 0 and a[i] % 13 == 0 and a[i] % 15 != 0 and a[i] % 17 != 0) or \
            (a[i + 1] % 11 == 0 and a[i + 1] % 13 == 0 and a[i + 1] % 15 != 0 and a[i + 1] % 17 != 0):
        c += 1
        summ = a[i] + a[i+1]
        minn = min(minn, summ)

print(c, minn)
