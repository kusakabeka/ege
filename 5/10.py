for x in range(10, 100):
    y = str(x % 2)
    y += str(x % 3)
    y += str(x % 5)
    if y == '104':
        print(x)
        break
