import re

def insert_spaces_in_camel(string):
    return re.sub(r'([a-z])([A-Z])', r'\1 \2', string)

m = input()
print(insert_spaces_in_camel(m))