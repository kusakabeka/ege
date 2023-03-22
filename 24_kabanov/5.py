with open("5.txt") as f: s = f.readline().replace("A", " ").replace("B", " ").replace("C", " ").split()
print(len(max(s, key=len)))