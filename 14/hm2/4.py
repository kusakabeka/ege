for x in "0123456789abcdef":
    n = int(f"1{x}bad", 16) + int(f"2c{x}fe", 16)
    if n % 15 == 0:
        ...
print((int(f"16bad", 16) + int(f"2c6fe", 16)) / 15)

