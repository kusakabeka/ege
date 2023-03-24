alf = [chr(i) for i in range(ord("A"), ord("Z") + 1)]
# for x in "0123456789ABCDEFGHIJK":
#     for y in "0123456789ABCDEFGHIJK":
#         n = int(f"12{y}{x}9", 21) + int(f"36{y}99", 21)
#         if n % 18 == 0:
#             pass
print((int(f"12539", 21) + int(f"36599", 21)) / 18)
