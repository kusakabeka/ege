import re

with open("2.txt") as f:
    s = f.readline()

substrings = re.findall(r"[^0]{1,2}0{0,2}", s)
max_length = max(len(substring) for substring in substrings)

print(max_length)
