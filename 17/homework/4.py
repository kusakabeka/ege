with open('17-1.txt') as f:
    a = list(map(int, f.readlines()))
c = 0
minn = 10000000
for i in range(len(a) - 1):
    if (str(a[i])[-1] == '7' and a[i] % 3 == 0) or (str(a[i+1])[-1] == '7' and a[i+1] % 3 == 0):
        c += 1
        minn = min(minn, min(a[i], a[i+1]))
print(c, minn)