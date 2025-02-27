import re

def replace_with_colon(string):
    return re.sub(r'[ ,.]', ':', string)

m = input()
print(replace_with_colon(m))