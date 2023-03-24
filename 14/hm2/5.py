for x in "0123456789abcdefg":
    n = int(f"9759{x}", 17) + int(f"3{x}108", 17)
    if n % 11 == 0:
        ...
# 2
print((int(f"97592", 17) + int(f"32108", 17)) / 11)
