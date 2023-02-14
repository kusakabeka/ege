n = 9 ** 18 + 3 ** 54 - 9
c = 0
while n > 0:
    if n % 3 == 2:
        c += 1
    n //= 3
print(c)