with open('24.txt') as f:
    s = ''.join(f.readlines())
s = s.split('AB')
for i in range(len(s)):
    summ = 0
    for j in range(i, i + 22):
        summ += len(s[j])