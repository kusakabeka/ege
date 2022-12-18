with open('24.txt') as f:
    a = f.readline()
a = a.replace('B', '$')[2:]
a = a.split('$')
a[:] = [x for x in a if x.strip()]
minn = 10000000
for i in range(len(a)):
    minn = min(len(a[i]), minn)
    print(minn)