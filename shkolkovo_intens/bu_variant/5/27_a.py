from itertools import permutations

f = open("27A.txt")
n = int(f.readline())

groupes = [[0, 0, 0]]

for t in f:
    new_groupes = []
    for last_group in groupes:
        s1, s2, s3 = last_group
        for a, b, c in permutations(list(map(int, t.split()))):
            new_groupes.append((s1 + a, s2 + b, s3 + c))
        groupes = {}
