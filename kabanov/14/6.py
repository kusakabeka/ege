for x in range(1, 100):
    t = (81 ** 20) - (9 ** x) + 50
    a = []
    while t > 0:
        a = [t % 9] + a
        t //= 9
    print(x, sum(a))