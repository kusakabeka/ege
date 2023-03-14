for n in range(1, 1000000):
    b = bin(n)[2:]
    b = b.replace("0", "*").replace("1", "0").replace("*", "1")
    b = '1' + b
    if b.count('1') % 2 == 0: b += '0'
    else: b += '1'
    r = int(b, 2)
    if r > 180:
        print(n)
        break