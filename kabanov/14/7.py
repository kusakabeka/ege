for x in range(1, 1000):
    t = oct(64 ** 12 - 8 ** 14 + x)
    if t.count("7") == 12 and t.count("1") == 1:
        print(x)
