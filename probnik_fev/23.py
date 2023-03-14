def f(x, y):
	# 1 to 34
	if x == y: return 1
	if x > y: return 0
	return f(x + 3, y) + f(x + 1, y) + f(x * 3, y)
print(f(1, 34))
# 329312