for n in range(2, 100):
    x = 338
    a = []
    while x > 0: a = [x % n] + a ; x //= n
    if a[-1] == 2 and len(a) == 3: print(n) 