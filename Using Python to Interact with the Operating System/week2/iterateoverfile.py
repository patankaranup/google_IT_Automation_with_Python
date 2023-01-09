with open('file1.txt', 'r') as file1:
    for line in file1:
        print(line.strip().upper())

file = open('file1.txt', 'r')
lines = file.readlines()
file.close()

print(sorted(lines))
