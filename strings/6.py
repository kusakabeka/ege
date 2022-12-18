s = input()
if s.count('f') == 1:
    print(s.index('f'))
elif s.count('f') >= 2:
    print(s.index('f'), s.rindex('f'))
elif s.count('f') == 0:
    print("")
