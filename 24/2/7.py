with open('7.txt') as f: s: str = f.readline()
cnt: int = 0 
c: int = 0
for i in range(len(s) - 1):
    if int(s[i]) < int(s[i + 1]): cnt  += 1
    else:
        if cnt == 5:
            ...
print(c)