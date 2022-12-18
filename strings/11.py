with open('24.txt') as f:
    s = "".join(f)
c = 0
a = []
for i in range(0, len(s)-1):
    a.append(s[i] + s[i+1])

for j in range(len(a)):
    if a[j] == "BA":
        c += 1
print(c)