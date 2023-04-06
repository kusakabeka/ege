for x in "0123456789ABCDEFGHI":
    n = int(f"55{x}36", 19) + int(f"{x}2724", 19)
    if n % 11 == 0:
        print(x)
# 6
print((int(f"55636", 19) + int(f"62724", 19)) / 11)
