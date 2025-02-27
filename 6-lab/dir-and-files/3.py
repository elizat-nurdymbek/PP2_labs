import os

path = input("Enter the path: ")

if os.path.exists(path):
    print("Path exists")
    print(f"Directory: {os.path.dirname(path)}")
    print(f"Filename: {os.path.basename(path)}")
else:
    print("Path does not exist")
