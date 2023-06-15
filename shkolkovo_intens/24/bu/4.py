with open("4.txt") as f: a = [l.rstrip() for l in f]

for i in a:
    if i.count("R") > 64:
        print(a)