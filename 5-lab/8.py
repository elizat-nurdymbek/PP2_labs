import re

def split_at_uppercase(string):
    return re.split(r'(?=[A-Z])', string)

m = input()
print(split_at_uppercase(m))