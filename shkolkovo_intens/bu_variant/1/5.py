for n in range(1, 100000):
    b = bin(n)[2:]
    if n % 2 != 0: b = "1" + b + "0"
    else: b = "1" + b + "1"

    r = int(b, 2)
    if r < 126:
        print(n)
        