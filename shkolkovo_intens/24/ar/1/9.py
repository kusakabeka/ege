with open("9.txt") as f: s = f.readline()
check_str = "AEIOYU"
c = 0
for i in s:
    if i in check_str:
        c += 1
print(c)