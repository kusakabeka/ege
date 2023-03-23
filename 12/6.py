s = "3" + "5" * 57
while "25" in s or "355" in s or "4555" in s:
    if "25" in s: s = s.replace("25", "3", 1)
    elif "355" in s: s = s.replace("355", "4", 1)
    elif "4555" in s: s = s.replace("4555", "2", 1)
print(s)
input()