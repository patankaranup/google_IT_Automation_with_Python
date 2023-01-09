import datetime
import os
size = os.path.getsize('./file2.txt')
print(size)
time = os.path.getmtime('./file2.txt')
print(time)  # seconds since 1st jan 1970
date = datetime.datetime.fromtimestamp(time)
print(date)
abs_path = os.path.abspath('./file2.txt')
print(abs_path)
