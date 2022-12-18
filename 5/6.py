for n in range(1, 10000):
    b = bin(n)[2:]
    b += b[-1]
    b = b + str(bin(n)[2:].count('1') % 2)
    b = b + str(bin(n)[2:].count('1') % 2)
    r = int(b, 2)
    if r > 80:
        print(r)
        break