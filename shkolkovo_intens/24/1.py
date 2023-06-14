from collections import Counter
c = 0
with open("test.txt") as file:
    s = [line.rstrip() for line in file]
for i in s:
    if i.count("N") < i.count("B"):
        c += 1
print(c)