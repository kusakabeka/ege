with open('11.txt') as f: s = f.readline().split()
print(len(max(s, key=len)))
