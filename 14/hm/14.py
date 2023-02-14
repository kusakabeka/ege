n = 49 ** 8 + 7 ** 24 - 7
c = 0
while n > 0:
    if n % 7 == 0:
        c += 1
    n //= 7
print(c)
