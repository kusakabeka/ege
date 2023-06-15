with open("4.txt") as f: s = f.readline()
max_len = 0
current_len = 1 
for i in range(len(s)):
    if s[i] == "M" and s[i + 1] == "M": current_len += 1
    else:
        max_len = max(max_len, current_len)
        current_len = 0
print(max_len)