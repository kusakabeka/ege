f = [0] * 40
f[1] = 1
f[2] = 1
for i in range(3, 40):
    if i % 2 != 0:
        f[i] = f[i - 1] + f[i - 2]
    else:
        f[i] = sum(f)

print(f)

