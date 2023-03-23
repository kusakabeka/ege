s = "687" * 143
while "68" in s or "7777" in s:
    s = s.replace("68", "7", 1)
    s = s.replace("7777", "7", 1)
print(s)