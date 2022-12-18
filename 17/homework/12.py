with open('17var13.txt') as f:
    a = list(map(int, f.readlines()))

c = 0
maxx = -10**6
for i in range(len(a) - 1):
    if a[i] < 450 and a[i+1] < 450:
        c += 1
        maxx = max(maxx, (a[i]**3 + a[i+1] ** 3))

print(c, maxx)