import re 

def match_a_b_zero_or_more(string):
    return bool(re.fullmatch(r'ab*', string))

m = input()
print(match_a_b_zero_or_more(m))