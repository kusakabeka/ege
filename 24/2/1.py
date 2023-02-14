from collections import Counter
f = open('1.txt')
c = 0
for s in f:
    if Counter(s)['E'] > Counter(s)['A']:
        c += 1
print(c)