s = input()
for i in s:
    if s.count('f') == 0:
        print()
    elif s.count('f') == 1:
        print(s.index('f'))
        break
    elif s.count('f') >= 2:
        s1 = s
        s = s.index('f')
        print(s)
        s1 = s1.rindex('f')
        print(s1)
        break
