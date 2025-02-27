my_list = list(map(int, input("Enter numbers separated by space: ").split()))

file_path = input("Enter the file path to save the list: ")

with open(file_path, 'w') as file:
    for item in my_list:
        file.write(f"{item}\n") 

print(f"List written to {file_path}")
