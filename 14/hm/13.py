n = 5 ** 36 + 5 ** 24 - 25
c = 0
while n > 0:
    if n % 5 == 4:
        c += 1
    n //= 5
print(c)

