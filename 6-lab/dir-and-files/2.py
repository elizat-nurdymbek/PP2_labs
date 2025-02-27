import os

path = input("Enter the path to check access: ")

print(f"Path Exists: {os.path.exists(path)}")
print(f"Readable: {os.access(path, os.R_OK)}")
print(f"Writable: {os.access(path, os.W_OK)}")
print(f"Executable: {os.access(path, os.X_OK)}")
