with open('17var5.txt') as f:
    a = list(map(int, f.readlines()))

c = 0
maxx = -10 ** 6
for i in range(len(a) - 1):
    if int(str(a[i])[-1]) == 5 and int(str(a[i + 1])[-1]) == 5:
        c += 1
        maxx = max(maxx, abs(a[i] - a[i+1]))
print(c, maxx)
