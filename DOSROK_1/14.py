for x in "0123456789abcd":
    n = int(f"97968{x}13", 15) + int(f"7{x}213", 15)
    if n % 14:
        print(n // 14)
        break
