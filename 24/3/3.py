from collections import Counter
with open('3.txt') as f: s = f.readline()
c = 0
arr = []
for i in range(1, len(s) - 1):
    if s[i-1] == 'A' and s[i+1] == 'C': arr.append(s[i])
print(Counter(arr))