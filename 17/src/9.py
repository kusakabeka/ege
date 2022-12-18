f = open('17-13.txt')
a = list(map(int, f.readlines()))

c = 0
maxs = -(10**6)

for i in range(len(a) - 1):
    for j in range(i+1, len(a)):
        if ((a[i] + a[j]) % 2 != 0) and ((a[i] + a[j]) > 0):
            maxs = max(maxs, a[i] + a[j])
            c += 1
print(c, maxs)