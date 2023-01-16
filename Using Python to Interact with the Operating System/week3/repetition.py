import re
# greedy
print(re.search(r"Py.*n", "Python Programmin"))
print(re.search(r"Py[a-z]*n", "Python"))
print(re.search(r"o+l+", "wooly"))
print(re.search(r"o+l+", "boil"))
