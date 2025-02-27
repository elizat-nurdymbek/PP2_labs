file_path = input("Enter the file path: ")

with open(file_path, 'r') as file:
    lines = file.readlines()
    print(f"Number of lines: {len(lines)}")
