with open("3.txt") as f: s = f.readline()
c = 0
while len(s) > 1:
    last_char = s[-1]
    if len(s) > 0 and s[0] == last_char:
        c += 1
    s = s[1:-1]
print(c)
