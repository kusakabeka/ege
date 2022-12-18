# s = input()
# print("for creeps")
# n, m = int(input()), int(input())
# print(len(s) - s.count(" "))
# print(s[2])
# print(True if s[0] == s[-1] else False)
# s_new = s[n:m+1]
# print(s_new)
with open("1.txt") as f:
    a = list(map(int, f.readlines()))
print(a)