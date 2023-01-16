import re


def has_aei_pattern(text):
    pattern = re.compile(r'a.e.i')
    match = pattern.search(text)
    return match is not None


print(re.search(r"[Pp]ython", "Python"))
print(re.search(r"[a-z]way", "The end of a highway"))
print(re.search(r"cloud[a-zA-z0-9]", "cloud6kafbew8"))
print(re.search(r"cat|dog", "I like cats "))
