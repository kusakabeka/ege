n = 9 ** 20 + 3 ** 60 - 125
c = 0
while n > 0:
    if n % 3 == 2:
        c += 1
    n //= 3
print(c)