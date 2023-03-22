with open("1.txt") as f: s = f.readline().replace("A", " ").replace("B", " ").split()
print(len(max(s, key=len)))