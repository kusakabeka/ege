import re
with open("4.txt") as f: s = f.readline()
s = re.split("E", s)
print(s)