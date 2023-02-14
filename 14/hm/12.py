n = 16 ** 18 * 4 ** 10 - 4 ** 6 - 16
c = 0
while n > 0:
    if n % 4 == 3:
        c += 1
    n //= 4
print(c)