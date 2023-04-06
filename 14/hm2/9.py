for x in "0123456789abcde":
    for y in "0123456789abd":
        M = int(f"2{y}23{x}5", 15)
        N = int(f"67{x}9{y}", 13)
        for A in range(1, 1000000):
            if (M + A) % N:
                print(A)
                break
