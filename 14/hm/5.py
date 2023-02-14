n = 49 ** 10 + 7 ** 30 - 49
c = 0
while n > 0:
    if n % 7 == 6:
        c += 1
    n //= 7
print(c)