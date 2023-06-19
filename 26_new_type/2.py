f = open("2.txt")
N, L, M = map(int, f.readline().split())
a = []
for i in range(N):
    st, r, t = f.readline().split()
    a.append([int(st), int(st) + int(r)])