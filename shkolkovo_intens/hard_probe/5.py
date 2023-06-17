for n in range(1, 1000):
    b = hex(n // 2)[2:]
    if n % 4 != 0: b = "F" + b + "A0"
    else: b = "15" + b + "C"
    r = int(b, 16)
    if r < 1048576:
        print(n)
'''
ans: 511
'''