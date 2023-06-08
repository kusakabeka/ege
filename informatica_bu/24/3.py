'''imports''' 
import re
from collections import Counter

'''file read'''
with open("1.txt") as f: a = [_.strip() for _ in f]
c = 0 
for i in range(len(a)):
	if a[i] == "G" and 