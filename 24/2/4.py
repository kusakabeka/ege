with open('4.txt') as f: s = f.readline()
a = []
local_max_1 = local_max_2 = 0
counter = 0
ans = ''
for i in range(1, len(s)):
    if s[i] > s[i - 1] and s[i] > s[i + 1]:
        ans += str(i) + ' '
print(ans)