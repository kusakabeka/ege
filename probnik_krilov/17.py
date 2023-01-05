with open('17.txt') as f:
    a = list(map(int, f.readlines()))
c = 0
maxx = max(a)
minn = 10 ** 11
for i in range(len(a)-2):
    if (str(a[i])[-1] != '3' and str(a[i + 1])[-1] != '3' and str(a[i + 2])[-1] != '3') and ((a[i] ** 2 + a[i+1] ** 2 + a[i + 2] ** 2) > maxx):
        c += 1
        minn = min(minn, (a[i] ** 2 + a[i+1] ** 2 + a[i + 2] ** 2))

print(c, minn)
