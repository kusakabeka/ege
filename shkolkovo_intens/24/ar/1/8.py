with open("8.txt") as f: s = f.readline()
ans = ""
a = []
for i in range(len(s) - 1):
    if s[i] == s[i + 1] and s[i + 2] != s[i]:
        ans += s[i] + s[i + 1] + " "
for j in ans.split():
    a.append(int(j))
print(sum(a))