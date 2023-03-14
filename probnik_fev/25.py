from fnmatch import *

for x in range(0, 10 ** 9, 151):
	if fnmatch(str(x), "2?34?56?8"):
		print(x, x // 151)