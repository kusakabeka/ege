for i in range(100, 1000):
    num_1 = int(str(i)[0]) * int(str(i)[1])
    num_2 = int(str(i)[1]) * int(str(i)[2])
    minn = min(num_2, num_1)
    maxx = max(num_2, num_1)
    number = str(minn) + str(maxx)
    if number == '615':
        print(i)
