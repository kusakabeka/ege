f = open("27B.txt")
k = int(f.readline())
n = int(f.readline())
a = [int(x) for x in f]
m_back = 0
m = 0
for i in range(k, n):
    m_back = max(m_back, a[i - k])
    m = max(m, m_back + a[i])
print(m)