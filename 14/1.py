a = 1*15**4 + 3*15**3 + 5*15**2 + 7
b = 7*15**4 + 5*15**2 + 3*15 + 1
summ = 0
for x in range(1, 15):
    sumnm = a + b + x * 15 + x * 15 ** 3
    if summ % 14 == 0:
        print(summ // 14)
        break
