file = open('file1.txt', 'r')
print(file.readline())
print(file.readline())
# continues to reading after the current cursor in the file
print(file.read())
file.close()

with open('file1.txt', 'r') as file1:
    print(file1.readline())
    print(file1.readline())
    # continues to reading after the current cursor in the file
    print(file1.read())
