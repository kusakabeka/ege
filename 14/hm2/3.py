c = 0
for x in "0123456789abc":
    n = int(f"186{x}4", 13) + int(f"5{x}716", 13)
    if n % 11 == 0:
        print(x)
        break
print((int(f"18644", 13) + int(f"54716", 13)) / 11)