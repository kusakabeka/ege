for x in "0123456789abcdefg":
    n = int(f"10{x}0", 17) + int(f"f0{x}ff", 17)
    if n % 13 == 0:
        x1 = x
        break
print((int(f"10{x1}0", 17) + int(f"f0{x1}ff", 17)) / 13)
