f = open('4.txt')
s = f.readline()

ans = ''
n = 0
nmax = 999999

for i in range(len(s)):
    if '0' <= s[i] <= '9':
        ans += s[i]
    elif ans != '':
        n = int(ans)
        if n % 2 != 0 and n < nmax:
            nmax = n
        k = ''
if k != '': 
    n = int(k)
    if n % 2 != 0 and n < nmax:
                nmax = n
print(nmax)
f.close()