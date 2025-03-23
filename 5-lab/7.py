import re

def snake_to_camel(snake_str):
    return ''.join(word.title() if i > 0 else word for i, word in enumerate(snake_str.split('_')))

m = input()
print(snake_to_camel(m))