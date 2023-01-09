import os
dir = "dir"
lists = os.listdir(dir)
for name in lists:
    fullname = os.path.join(dir, name)
    if os.path.isdir(fullname):
        print(f"{fullname} is a directory")
    else:
        print(f"{fullname} is a file")
