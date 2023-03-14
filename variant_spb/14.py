for x in "0123456789abcd":
    n = int(f"753{x}2", 13) + int(f"2{x}173", 13)
    if n % 12 == 0:
        print(x)
        break
print((int(f"75332", 13) + int(f"23173", 13)) / 12)