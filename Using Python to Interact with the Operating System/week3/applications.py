import re
print(re.search(r"A.*a", "Argentina"))
print(re.search(r"A.*a", "Azerbaijan"))
# to make it stricter $
print(re.search(r"A.*a$", "Azerbaijan"))


# for validating variable name ^ should start with and end with $
pattern = r"^[a-zA-Z_][a-zA-Z0-9_]*$"
print(re.search(pattern, "_this_is_valid_variable_name"))
print(re.search(pattern, "this is not a var name"))
