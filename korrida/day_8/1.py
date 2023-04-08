f = open('1.txt')
s = f.readline()
f.close()
a, maxim = s[0], 0
for i in range(len(s) - 1):
    if s[i] > s[i + 1]:
        a += s[i+1]
    else:
        if len(a) > maxim:
            rez = a
            maxim = len(a)
        a = s[i+1]
if len(a) > maxim:
    rez = a
print(rez)