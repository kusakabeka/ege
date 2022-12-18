with open('24 - 1.txt') as f:
    a = f.readline().split(" ")
for i in range(len(a)):
    print(*a)