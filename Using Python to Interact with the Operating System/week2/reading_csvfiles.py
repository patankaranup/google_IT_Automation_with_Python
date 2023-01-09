import csv
file = open('names.txt')
csv_file = csv.reader(file)
for row in csv_file:
    name, marks = row
    print(f"Name :{name} Row :{marks}")
file.close()
