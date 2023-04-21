with open("sample_24.txt") as f: s = f.readline().replace("A", " ")
a_indexes = []
for i in range(len(s)):
        if s[i] == "A":
                print()
