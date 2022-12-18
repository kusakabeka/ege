with open('24.txt') as f:
    s = f.readline()
s = s.replace('B', ' ').split(" ")
s[:] = [x for x in s if x.strip()]
for i in range(len(s)):
    print(*s[i])