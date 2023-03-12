f = open("27-A.txt")
s = f.readlines()
string, a = "", []
for _ in range(len(s)):
    string += s[i]
string = string.split('\n')[:-1]
for _ in range(len(string)):
    a.append(int(string[i]))
for i in range(len(a) - 1):
    for j in range(i, len(a) - 1):
        if a[i] + a[j] % 2 == 0:
