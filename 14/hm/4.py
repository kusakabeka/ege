n = 49 ** 7 + 7 ** 21 - 7
c = 0
while n > 0:
    if n % 7 == 6:
        c += 1
    n //= 7
print(c)