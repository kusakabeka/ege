with open('17-1.txt') as f:
    a = list(map(int, f.readlines()))

c = 0
minn = 100000000
for i in range(len(a) - 2):
    if a[i] < a[i+1] < a[i+2]:
        c += 1
        minn = min(minn, )