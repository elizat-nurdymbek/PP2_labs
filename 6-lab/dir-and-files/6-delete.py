import os
import string

letters = string.ascii_uppercase  

for letter in letters:
    file_name = f"{letter}.txt"
    
    if os.path.exists(file_name):
        os.remove(file_name)
        print(f"Deleted {file_name}")
    else:
        print(f"{file_name} does not exist")
