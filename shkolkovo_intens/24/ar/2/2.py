with open("2.txt") as f: s = f.readline()

local_minimums_numbers_indexs = []

for i in range(1, len(s) - 1):
    if (s[i] <= s[i - 1]) and (s[i] <= s[i + 1]):
        local_minimums_numbers_indexs.append(i)
        
for i in range(len(local_minimums_numbers_indexs)):
    ...