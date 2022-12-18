with open('17.txt') as f:
    a = list(map(int, f.readlines()))

cnt = 0
summ = 0
for i in range(len(a)):
    if a[i] % 2 == 0:
        cnt += 1
        summ += a[i]
sr = summ // cnt

c = 0
maxx = 0
for i in range(len(a) - 1):
    if (a[i] % 3 == 0 or a[i+1] % 3 == 0) and \
            (a[i] <= sr or a[i+1] <= sr):
        c += 1
        maxx = max(maxx, a[i] + a[i+1])

print(c, maxx)