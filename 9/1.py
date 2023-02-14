import csv

with open('9.csv', newline = '') as f:
    reader = map(int, csv.reader(f, delimiter=';'))
    c = 0
    for row in reader:
        print(f'{type(int(row[0]))} - {int(row[0])} \n')