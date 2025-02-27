import re

def match_a_anything_b(string):
    return bool(re.fullmatch(r'a.*b', string))

m = input()
print(match_a_anything_b(m))