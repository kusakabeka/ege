with open("24.txt") as f: s = f.readline().replace("000", "** **").split(" ")
print(len(max(s, key=len)))
