f = open("...")
n = int(f.readline())
k = [0] * 100
for i in range(n):
    x = int(f.readline())
    ost = x % 100
    k[ost] += 1

count = 0
for i in range(0, 100):
    count += k[i] * (k[i] - 1)
print(count)
