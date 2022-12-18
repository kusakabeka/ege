def filter_odd_num(in_num):
    return True if(in_num % 2) != 0 else False

with open('17.txt') as f:
    a = list(map(int, f.readlines()))

minimal = min(list(filter(filter_odd_num, a)))
c = 0
maxx = 0
for i in range(len(a) - 1):
    if ((a[i] % 3 == 0 and a[i+1] % 3 != 0) or \
        (a[i+1] % 3 == 0 and a[i+1] % 3 != 0)) and \
            (abs(a[i] - a[i+1] < minimal)):
        c += 1
        maxx = max(maxx, abs(a[i]) - abs(a[i+1]))
print(c, maxx)