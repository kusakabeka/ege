with open("2.txt") as f: s = f.readline().replace("D", " ").replace("C", " ").split()
print(len(max(s, key=len)))
