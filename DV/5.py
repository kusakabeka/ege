# задание на двоичную запись 
for n in range(1, 1000000):
    b = bin(n)[2:]
    if n % 3 == 0: b += b[-3:]
    else: b += bin(3 * (n % 3))[2:]
    r = int(b, 2)
    if r < 170:
        print(f"n:{n} - r:{r}")