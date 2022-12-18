start = 1
finish = 32
a = [0] * (finish + 1)
a[1] = 1
for i in range(start + 1, finish + 1):
    a[i] += a[i-1]
    if i % 4 == 0:
        a[i] += a[i // 4]

print(a)
