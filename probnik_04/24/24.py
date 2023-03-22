with open("24.txt") as f: s = f.readline().replace('B', 'C')
s = s.replace("CCA", '*').replace("A", " ").replace("C", " ").split()
#print(len(max(s, key=len)))
print(len(max(s, key=len)*3))