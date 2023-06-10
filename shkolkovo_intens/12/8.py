s = ""
while "LL" in s:
    s = s.replace("BU", "LL", 1)
    if "BULL" not in s:
        s = s.replace("LLLLLL", "CAT", 1)
