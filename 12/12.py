s = "0" + "1" * 20 + "2" * 10 + "3" * 70
while "01" in s or "02" in s or "03" in s:
    s = s.replace("01", "30", 1)
    s = s.replace("02", "101", 1)
    s = s.replace("03", "202", 1)
print(s.count("1"))