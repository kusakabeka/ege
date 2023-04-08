with open('24.txt') as f:
   k = 0
   s = f.readline()
   s = s.split('E')
   for i in range(1,len(s)-1):
       if len(s[i]) >= 10 and s[i].count('F')==0:
           k +=1
   print(k)

#123
#49234
#9655