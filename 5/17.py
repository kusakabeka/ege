for n in range(1, 100000):
    b = bin(n)[2:]
    b1 = b.replace('0', '00')
    b1 = b1.replace('1', '11')
    r = int(b1, 2)
    if r > 32:
        print(r)
        break