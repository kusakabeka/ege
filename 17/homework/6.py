with open('17-1.txt') as f:
    a = list(map(int, f.readlines()))
c = 0
maxx = 0
for i in range(len(a) - 1):
    if a[i] % 3 == 0 or a[i+1] % 3 == 0:
        if a[i] + a[i+1] <= (max(a[i], a[i+1]) % 3 == 0):
            c += 1
            maxx = max(maxx, a[i] + a[i+1])
print(c, maxx)