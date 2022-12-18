s = input()
s1 = s
for i in range(len(s)):
    if s[i].isdigit():
        s1 = s1.replace(s[i], '', 1)

print(s1)