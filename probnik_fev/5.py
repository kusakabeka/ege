for n in range(1, 10000000):
    b = bin(2 * n)[2:]
    b += str(b.count('1(эффективный перебор)') % 2)
    b += str(b.count('1(эффективный перебор)') % 2)
    r = int(b, 2)
    if r > 249:
        print(n)
        break