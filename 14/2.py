a = 1*17**4 + 3*17**3 + 5*17**2 + 9
b = 9*17**4 + 5*17**2 + 3*17 + 1
for x in range(0 , 17):
    summ = a + b + x * 17 + x * 17 ** 3
    if summ % 9 == 0:
        print(summ // 9)
