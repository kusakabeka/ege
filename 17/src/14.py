f = open('17-9.txt')
a = list(map(int, f.readlines()))


def k_0(n):
    return bin(n)[2:].count('0') >= 1


def k_1(n):
    return bin(n)[2:].count('1') == 2


c = 0
maxs = 0
s = 0
for i in range(len(a) - 2):
    s = 0
    if k_1(a[i]) and k_0(a[i]):
        s += 1
    if k_1(a[i + 1]) and k_0(a[i + 1]):
        s += 1
    if k_1(a[i + 2]) and k_0(a[i + 2]):
        s += 1
    if s >= 2:
        c += 1
        maxs += max(a[i], a[i + 1], a[i + 2])
print(c, maxs)