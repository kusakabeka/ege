import re
from typing import Final
f = open("4.txt")
reg = "F\.O"
c = 0
while True:
    s = f.readline()
    if reg in s:
        c += 1

print(c)