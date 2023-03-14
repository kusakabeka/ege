a = list(map(int, open("17.txt")))
def sorrt(n): 
    if n % 3 == 0: return n
numbers = list(filter(sorrt, a))
maxx = 0
c = 0
for i in range(len(a) - 1):
    if (a[i] < 0 or a[i + 1] < 0) and (a[i] + a[i + 1] < len(numbers)):
        maxx = max(maxx, a[i] + a[i + 1])
        c += 1
print(c, maxx)
