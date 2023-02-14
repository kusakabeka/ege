with open('4.txt') as f: s = f.readline()
ans = ''
for i in range(1, len(s)):
    if ord([i-1]) > ord([i]):
        ...