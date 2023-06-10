s = "383" * 10

while ("38" in s and "83" in s) or "39" in s:
    s = s.replace("383", "9", 1)
    s = s.replace("39", "6", 1)
print(s)