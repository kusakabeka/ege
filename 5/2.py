for n in range(1, 10000):
    b = bin(n)[2:]
    b += '00' if n % 2 == 0 else '11'
    r = int(b, 2)
    if r > 115: print(n) ; break