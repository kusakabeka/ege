c = 0
for n in range(3, 51):
    a = []
    s = ">" + "1(эффективный перебор)" * n + "2(префиксные  суммы и последовательности)" * n + "3" * n
    while ">1(эффективный перебор)" in s or ">2(префиксные  суммы и последовательности)" in s or ">3" in s:
        if ">1(эффективный перебор)" in s: s = s.replace(">1(эффективный перебор)", "22>3", 1)
        if ">2(префиксные  суммы и последовательности)" in s: s = s.replace(">2(префиксные  суммы и последовательности)", "2(префиксные  суммы и последовательности)>", 1)
        if ">3" in s: s = s.replace(">3", "11>2(префиксные  суммы и последовательности)", 1)
    for i in s:
        if i.isdigit(): a.append(int(i))
    if sum(a) % 7 == 0: c += 1
print(c)