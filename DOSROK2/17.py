with open("17.txt") as f: s = f.readlines()
for j in range(len(s)):
    s[j] = int(s[j].strip())
max_el = max([s[k] for k in range(len(s)) if len(str(s[k])) == 2])
m = c = 0
for i in range(len(s) - 1):
    if ((len(str(s[i])) == 2 and len(str(s[i + 1])) != 2) or (len(str(s[i])) != 2 and len(str(s[i + 1])) == 2)) and (s[i] + s[i+1]) % max_el == 0:
        c += 1
        m = max(m, s[i] + s[i + 1])
print(c, m)