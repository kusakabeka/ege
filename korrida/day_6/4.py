with open("4.txt") as f: s = f.readline().split()
print(len(max(s, key=len)))