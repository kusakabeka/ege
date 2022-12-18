f = open('17-10.txt')
a = list(map(int, f.readlines()))

c = 0
s = 0

for i in range(len(a) - 2):
    if a[i] > a[i + 1] > a[i + 2]:
        if a[i] % 3 == 0 or a[i + 1] % 3 == 0 or a[i + 2] % 3 == 0:
            c += 1
            s = max(s, a[i] + a[i + 1] + a[i + 2])
print(c, s)
