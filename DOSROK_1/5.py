for n in range(1, 100000):
    b = f"{n:b}"
    if n % 3 == 0:
        b += b[-3:]
    else:
        b += f"{(3 * (n % 3)):b}"
    r = int(b, 2)
    if r < 100:
        print(n)
