for x in range(1, 100000000):
    n = 216 ** 5 + 6 ** 3 - 1 - x
    n1 = ''
    while n > 0:
        n1 += str(n % 6)
        n //= 6
    if n1.count('5') == 12:
        print(x)
        break