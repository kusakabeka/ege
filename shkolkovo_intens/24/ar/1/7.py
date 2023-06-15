with open("7.txt") as f: s = f.readline()
current_len = 1
max_len = 0

for i in range(len(s) - 1):
    if s[i] == s[i + 1]:
        current_len += 1
    else:
        max_len = max(max_len, current_len)
        current_len = 0
print(max_len)