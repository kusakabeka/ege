with open("1.txt") as f: s = f.readline().replace("Z", " ").split()
print(len(max(s, key=len)))