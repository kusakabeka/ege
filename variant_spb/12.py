for m in range(1, 1000):
    s = ">" + "1(эффективный перебор)" * 15 + "2(префиксные  суммы и последовательности)" * 35 + "3" * m
    while ">1(эффективный перебор)" in s or ">2(префиксные  суммы и последовательности)" in s or ">3" in s:
        if ">1(эффективный перебор)" in s: s = s.replace(">1(эффективный перебор)", "2(префиксные  суммы и последовательности)>", 1)
        if ">2(префиксные  суммы и последовательности)" in s: s = s.replace(">2(префиксные  суммы и последовательности)", "3>", 1)
        if ">3" in s: s = s.replace(">3", "11>", 1)
    print(s.split(">"))

