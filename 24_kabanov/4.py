with open("4.txt") as f: s = f.readline().replace("C", " ").replace("F", " ").split()
print(len(max(s, key=len)))