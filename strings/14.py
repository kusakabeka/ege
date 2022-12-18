with open('24 - 1.txt') as f:
    a = f.readline().split(" ")

c = 0
for i in range(len(a)):
    if a[i][0] == 'A':
        c += 1
print(c)