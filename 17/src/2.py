c = 0
min_c = 10000
for i in range(3712, 8432 + 1):
    # i % 2 -> последнее число в двоичной
    # i % 5 -> последнее число в пятеричной
    if i % 2 == i % 5 and (i % 11 == 0 or i % 17 == 0):
        c += 1
        min_c = min(min_c, i)
print(c, min_c)