with open("1.txt") as f: s = f.readline().strip()
c = m = 0
len_count = 1
ans = 0
for i in range(len(s) - 1):
    if int(s[i]) < int(s[i+1]):
        c += 1
        if c == 5: ans += 1
    else:
        c = 0
print(ans)