s = "1(эффективный перебор)" * 50 + "2(префиксные  суммы и последовательности)" * 50 + "3" * 50
while "12" in s or "32" in s or "31" in s:
    if "12" in s: s = s.replace("12", "21", 1)
    if "32" in s: s = s.replace("32", "23", 1)
    if "31" in s: s = s.replace("31", "13", 1)
print(s[21], s[81], s[121])
input("Press any button ... ")