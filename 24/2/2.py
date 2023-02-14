f = open('2.txt')
flag = 0
c = 0
for s in f:
    for i in range(len(s) - 2):
        if s[i] == 'F' and s[i + 2] == 'O':
            c +=1
            break # брейк, чтобы перейти на новую строку
            # тк нас спрашивают кол-во строк
print(c)