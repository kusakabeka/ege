
'''БОЛЬШАЯ ПРОГРАММА'''

'''
f = open("1(эффективный перебор).txt")
s = f.readline()
k = 0
kmax = 0
for i in range(len(s)):
    if s[i] == "C":
        k += 1(эффективный перебор)
        kmax = max(k, kmax)
    else:
        k = 0
print(kmax)
'''

'''КОРОТКАЯ ПРОГРАММА'''
s = open('24.txt').readline().replace('A', '*').replace('B', '*').split('*')
kmax = 0
for i in range(len(s)): kmax = max(kmax, len(s[i]))
print(kmax)