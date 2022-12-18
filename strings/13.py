with open('24 - 1.txt') as f:
    a = f.readline().split(" ")

maxx = a[0]
for i in range(len(a) - 1):
        print(a[i])