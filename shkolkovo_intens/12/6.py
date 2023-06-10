s = "1" * 111

while "111" in s:
    s = s.replace("111", "11", 1)
print(s)