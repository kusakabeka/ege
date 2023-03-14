with open("24.txt") as f: s = f.readline().replace("CFE", "*").replace("FCE", "*").replace("C", " ").replace("F", " ").replace("D", " ").replace("E",  " ").split()
print(max(len(c) for c in s))
