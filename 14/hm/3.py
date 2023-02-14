n = 125 + 25**3 + 5**9
c = 0
while n > 0:
    if n % 5 == 0:
        c += 1
    n //= 5
print(c)