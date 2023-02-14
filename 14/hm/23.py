for x in range(1, 100000000):
    n = 343 ** 5 + 7 ** 3 - 1 - x
    n1 = ''
    while n > 0:
        n1 += str(n % 7)
        n //= 7
    if n1.count('6') == 12:
        print(x)
        break