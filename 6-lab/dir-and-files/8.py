import os

file_path = input("Enter the file path to delete: ")

if os.path.exists(file_path):
    if os.access(file_path, os.W_OK):
        os.remove(file_path)
        print(f"File '{file_path}' deleted successfully.")
    else:
        print("You do not have permission to delete this file.")
else:
    print("File does not exist.")
