s = "9" * 185
while "9999" in s or "333" in s:
    if "9999" in s: s = s.replace("9999", "3", 1)
    else: s = s.replace("333", "99", 1)
print(s)
input()