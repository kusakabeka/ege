def dell(x, a):
    return x % a == 0


A = 1
while True:
    for x in range(1, 1_000_000):
        if not ((not dell(x, A)) <= (dell(x, 6) <= (not dell(x, 4)))):
            break
    else:
        print(A) # 12
    A += 1
