f = open('17-243.txt')
a = list(map(int, f.readlines()))

max_119 = 0
for i in range(len(a)):
    if a[i] % 119 == 0:
        max_119 = max(max_119, a[i])

c = 0
mins = 10 ** 6
for i in range(len(a) - 1):
    if (a[i] > max_119 or a[i+1] > max_119) and (a[i] % 100 == 21 or a[i+1] % 100 == 21):
        c += 1
        mins = min(mins, a[i] + a[i+1])

print(c, mins)