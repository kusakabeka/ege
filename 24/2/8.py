f = open('8.txt')
c = m = 0
for s in f:
    for i in range(len(s) - 1):
        if int(s[i]) + int(s[i+1]) >= 10:
            c += 1
            m = max(m, c)
        else:
            c = 0
print(m)

# 1345563211