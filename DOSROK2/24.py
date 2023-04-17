with open('24.txt', 'r') as f: s = f.readline().replace("X", "Z").replace("Y", "Z").replace("ZZ", "Z Z").split()
print(len(max(s, key=len)))