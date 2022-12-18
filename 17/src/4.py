f = open('17-4.txt')
a = list(map(int, f.readlines()))
max_11 = 0
c = 0
min_c = 10 ** 6
for i in range(len(a)):
    if a[i] % 11 == 0: max_11 = max(max_11, a[i])

for i in range(len(a) - 1):
    if a[i] > max_11 or a[i + 1] > max_11:
        c += 1
        min_c = min(min_c, a[i] + a[i + 1])

print(c, min_c)

f.close()
