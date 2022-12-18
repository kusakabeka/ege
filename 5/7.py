for n in range(256):
    b = bin(n)[2:]
    b = '0' * (8 - len(b)) + b
    b1 = b.replace('0', '*')
    b1 = b1.replace('1', '0')
    b1 = b1.replace('*', '1')
    r = int(b1, 2)
    razn = r - n
    if razn == 113:
        print(n)
