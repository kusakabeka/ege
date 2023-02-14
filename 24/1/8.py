with open('8.txt') as f:
    s = f.readline()

c = 0
s = s.replace('XVI', '*')
print(s.count('*'))
