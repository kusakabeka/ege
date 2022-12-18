f = open('17-10.txt')
a = list(map(int, f.readlines()))

c = 0
s = 0

for i in range(len(a) - 2):
    if a[i] % 5 == 0 or a[i+1] % 5 == 0 or a[i+2] % 5 == 0:
        c += 1
        s += min(a[i], a[i+1], a[i+2])

print(c, s)