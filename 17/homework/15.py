f = open('17.txt')
s = list(map(int, f.readlines()))
k = 0
m = 10001
for i in range(len(s)):
    if s[i] % 2 != 0 and s[i] < m:
        m = s[i]
count = 0
mx = 0
for i in range(len(s) - 1):
    if (s[i] % 3 == 0 and s[i + 1] % 3 != 0 and abs(s[i] - s[i + 1]) < m) or (
            s[i + 1] % 3 == 0 and s[i] % 3 != 0 and abs(s[i] - s[i + 1]) < m):
        count += 1
        mx = max(mx, abs(s[i] - s[i + 1]))
print(count, mx)
