for n in range(1, 1000000):
    b = bin(n)[2:]
    if n % 11 == 0: b += "0" * b.count("0")
    else: b  = "1" * b.count("1") + b
    r = int(b, 2)
    if r % 227 == 0:
        print(n)
        break

