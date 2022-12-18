s = input()
c = 0
summ = 0
for i in range(len(s)):
    if s[i].isdigit():
        c += 1
        summ += int(s[i])

print(c, summ)