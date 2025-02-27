import re

def find_lowercase_with_underscore(string):
    return re.findall(r'\b[a-z]+_[a-z]+\b', string)

m = input()
print(find_lowercase_with_underscore(m))