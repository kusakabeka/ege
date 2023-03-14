for n in range(100000):
    try:
        if int("123", n) == int("93", n + 2):
            print(n)
    except:
        pass