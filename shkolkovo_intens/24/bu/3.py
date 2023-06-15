with open("3.txt") as f: a = [l.rstrip() for l in f]
c = 0
for i in range(len(a) - 3):
    if a[i] == "T" and a[i + 3] == "O":

