import csv
filename = "sample csv.csv"
# I have taken a sample csv from internet
with open(filename, 'r') as file:
    csv_reader = csv.reader(file)
    for row in csv_reader:
        print(row)
