s1, s2 = int(input()), int(input())
arr = [_ for _ in range(1, 11)]
x = 0
cnt = 0
for j in range(s1-1, s2):
  x += arr[j]
  cnt += 1
ans = x / cnt
print('%.2f' % ans)