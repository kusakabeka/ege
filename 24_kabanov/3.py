with open("3.txt") as f: s = f.readline().replace("D", " ").split()
print(len(max(s, key=len)))