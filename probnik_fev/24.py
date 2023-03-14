with open("24.txt") as f: s = f.readline().replace('O', 'A').replace('F', 'C').replace('D', 'C')
s = s.replace("CAAC", 'CAA AAC').split()
print(len(max(s, key=len)))