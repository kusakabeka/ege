with open('5.txt') as f:
    s = f.readline()
c = 0
for i in range(len(s) - 2):
    if s[i] == 'K' and s[i + 1] == 'O' and s[i + 2] == 'T':
        c += 1
        print(c)