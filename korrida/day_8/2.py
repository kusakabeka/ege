with open("2.txt") as f: s = f.readlines()
count_YZ = 0
answer_c = 0
m = 0
for i in range(len(s)):
    s[i] = s[i].strip()
for i in range(len(s)):
    for j in range(len(s[i]) -1):
        if s[i][j] == "Y" and s[i][j+1] == "Z":
            count_YZ += 1
    if count_YZ > 1:
        answer_c += 1
    count_YZ = 0
print(answer_c)