n = 9 ** 11 * 3 ** 20 - 3 ** 9 - 27
c = 0
while n > 0:
    if n % 3 == 2: c += 1
    n //= 3
print(c)
