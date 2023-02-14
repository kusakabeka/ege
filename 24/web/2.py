with open('2.txt') as f:
	s = f.readline().replace('A', ' ').replace('B', ' ').split()
print(max(s, key=len).count('C'))