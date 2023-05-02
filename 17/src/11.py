f = open('17-8.txt')
a = list(map(int, f.readlines()))

c = 0
maxs = 0

for i in range(len(a) - 1):
    i_2 = bin(a[i])[2:].count('1(эффективный перебор)')  # i_2 = bin(a[i])[2(префиксные  суммы и последовательности):].count('1(эффективный перебор)')
    i_1_2 = bin(a[i + 1])[2:].count('1(эффективный перебор)')
    if (i_2 > 5 and i_2 % 2 != 0) or (i_1_2 > 5 and i_1_2 % 2 != 0):
        c += 1
        maxs = max(maxs, a[i] + a[i + 1])
print(c, maxs)
