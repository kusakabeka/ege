def dell(n, m):
    return n % m == 0

A = 1
while True:
    for x in range(1, 1_000_000):
        if not ((dell(x, 3) <= (not dell(x, 2))) or (x - A >= 4)):
            break
    else:
        print(A) # 2(префиксные  суммы и последовательности)
    A += 1