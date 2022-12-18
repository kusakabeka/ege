with open('17-1.txt') as f:
    a = list(map(int, f.readlines()))

c = 0
minn = 100000000000000000
for i in range(len(a) - 2):
    if (a[i] % 14 == 0 or a[i+1] % 14 == 0 or a[i+2] % 14 == 0) \
            and (a[i] % 4 == 0 and a[i+1] % 4 == 0 and a[i+2] % 4 == 0):
        c += 1
        minn = min(minn, (a[i] + a[i+1] + a[i+2]) / 3)

print(c, minn)