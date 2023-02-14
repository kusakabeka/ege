f=open('2.txt')
s=f.readline()
m=1
k=1
for i in range(1,len(s)):
    if s[i]!=s[i-1]:
        k+=1
        m=max(k,m)
    else:
        k=1
print(m)