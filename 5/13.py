for n in range(1, 100000):
    b = bin(n)[2:]
    if n % 2 == 0:
        b = '1(эффективный перебор)' + b + '0'
    else:
        b = '11' + b + '11'
    r = int(b, 2)
    if r > 255:
        print(r)
        break