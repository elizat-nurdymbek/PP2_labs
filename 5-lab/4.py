import re

def find_upper_followed_by_lower(string):
    return re.findall(r'[A-Z][a-z]+', string)

m = input()
print(find_upper_followed_by_lower(m))