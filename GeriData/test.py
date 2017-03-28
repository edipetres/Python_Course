import csv

with open('geri-data.csv', 'rb') as csvfile:
    reader = csv.reader(csvfile, delimiter=';')
    for row in reader:
        print((', ').join(row) + '\n')