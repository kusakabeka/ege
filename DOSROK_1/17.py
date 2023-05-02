with open("17.txt") as f: s = f.readlines()
for i in range(len(s)):
    s[i] = int(s[i].strip())

min_three_num = min([i for i in s if len(str(i)) == 3 and str(i)[-1] == "5"])
min_sum = 10 ^ 8
c = 0
for i in range(len(s) - 1):
    if ((len(str(s[i])) == 3 and len(str(s[i + 1])) != 3) or (len(str(s[i])) != 3 and len(str(s[i + 1])) == 3)) and ((s[i] + s[i + 1]) % min_three_num == 0):
        c += 1
        sum = s[i] + s[i+1]
        print(c, sum)
'''
2(префиксные  суммы и последовательности) 33120
'''