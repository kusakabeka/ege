s = "8" * 100
while "888" in s or "77" in s:
    if "888" in s: s = s.replace("888", "8777", 1)
    else: s = s.replace("77", "8", 1)
print(s.count('8'), s.count("7"))
