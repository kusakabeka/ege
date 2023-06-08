from collections import Counter
with open("4.txt") as f: p = [_.strip() for _ in f]
'''
sort lines
'''
a = []
for i in p:
	if Counter(i)["N"] > 50: a.append(i)

#print(Counter(a[0])["N"])

def is_true(a: list) -> bool:
	sample_c = 0
	for i in range(len(a)):
		if Counter(a[i])["N"] > 50:
			sample_c += 1
	if sample_c == len(a):
		return True

'''
....


'''
def sort_index(s: str) -> dict:
	sample_arr = []
	for i in range(len(s)):
		if Counter(s)[s[i]] > 1: sample_arr.append(s[i])
	
'''
d = dict("a": [1, 6, 9], "d": [1, 5])

=> 
last_index - first_index


'''

print(sort_index("abcdeafkad"))

'''
s = "abcbcadfbcadfhbacb"

{'a': 4, 'b': 5, 'c': 4, 'd': 2, 'f': 2, 'h': 1}

'''
