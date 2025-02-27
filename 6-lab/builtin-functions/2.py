def count_case(s):
    upper_count = sum(1 for c in s if c.isupper())
    lower_count = sum(1 for c in s if c.islower())
    return upper_count, lower_count

text = input()
upper, lower = count_case(text)
print(f"Upper case: {upper}, Lower case: {lower}")  
