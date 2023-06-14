for A in range(1, 101):
    f = 0
    for x in range(1,1001):
        if (((x % A != 0) and (x % 6 == 0)) <= (x % 3 != 0)) == False:
            f = 1
    if f == 0:
        print(A)