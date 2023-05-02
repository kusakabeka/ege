for n in range(1, 100000):
    b = bin(n)[2:]
    sr = len(b) // 2
    if len(b) % 2 == 0:
        b = b[0: sr] + '1(эффективный перебор)' + b[sr:]
    r = int(b, 2)
    if r <= 26:
        print(n)
        # 26
        
