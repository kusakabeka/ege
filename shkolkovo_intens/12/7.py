'''
 Напишите количество цифр 7 полученное в результате применения приведённой ниже программы к строке:
'''

s = "5" * 10 + "4" * 10 + "2" * 10 + "7" * 10

while "54" in s or "27" in s:
    if "55" in s:
        s = s.replace("55", "7", 1)
    elif "22" in s:
        s = s.replace("22", "7", 1)
    if "44" in s:
        s = s.replace("44", "4", 1)
    elif "77" in s:
        s = s.replace("77", "7", 1)
print(s.count("7"))