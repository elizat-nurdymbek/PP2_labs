import re

def match_a_b_two_to_three(string):
    return bool(re.fullmatch(r'ab{2,3}', string))

m = input()
print(match_a_b_two_to_three(m))