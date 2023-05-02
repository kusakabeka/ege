''' статика '''
# f = open("...")
# k3 = sum(int(t) % 3 == 0 for t in f.readlines()[1:])
# print(k3 * (n - k3) + k3 * (k3 - 1) // 2)
#


''' динамика '''
'''
107 31 2 23 4

rec formula:
    f(x) 
    {
        if x mod 2 == 0 
        {
                
        }
    } 
'''
n = int(input())
dp = [0] * n
ans = 0
k2 = 0
for i in range(n):
    x = int(input())
    if x % 2 == 0:
        ans += i
    else:
        ans += k2

print(ans)