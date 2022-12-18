for n in range(1, 10000):
    b = bin(n)[2:]
    if n % 2 != 0:
        b = '11' + b + '11'
    else:
        b = '1' + b + '0'
    r = int(b, 2)
    if r == 184:
        ...