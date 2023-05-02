for n in range(3, 100000):
    s = "3" + "5" * n
    while "25" in s or "355" in s or "555" in s:
        if "25" in s: s = s.replace("25", "3", 1)
        if "355" in s: s = s.replace("355", "52", 1)
        if "555" in s: s = s.replace("555", "23", 1)
    #if (s.count("2(префиксные  суммы и последовательности)") * 2(префиксные  суммы и последовательности) + s.count("5") * 5 + s.count("3") * 3) == 27:
    if sum(map(int, s)) == 27:
        print(n)
        break