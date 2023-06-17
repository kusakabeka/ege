with open("2.txt") as f: s = f.readline()

indexs = []

for i in range(1, len(s) - 1):
    if (s[i] <= s[i - 1]) and (s[i] <= s[i + 1]):
        indexs.append(i)
    
c_l = 0
m_l = 0
for i in range(len(indexs) - 1):
    c_l = indexs[i + 1] - indexs[i]
    m_l = max(m_l, c_l)
print(m_l)