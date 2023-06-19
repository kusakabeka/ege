for x in "0123456789abcdefghi":
    n = int(f"98{x}79641", 19) + int(f"36{x}14", 19) + int(f"73{x}4", 19)
    if n % 18 == 0:
        print(f"x:{x} - n:{n // 18}")
        