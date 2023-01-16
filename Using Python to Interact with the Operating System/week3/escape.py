import re

print(re.search(r".com", "welcome"))
print(re.search(r"/.com", "welcome"))
print(re.search(r".com", "www.google.com"))
print(re.search(r"\w*", "This is a line"))
print(re.search(r"\w*", "A_Word"))
