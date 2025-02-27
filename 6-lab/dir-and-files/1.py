import os

path = input("Enter the path: ")

# List only directories
print("\nDirectories:")
print([d for d in os.listdir(path) if os.path.isdir(os.path.join(path, d))])

# List only files
print("\nFiles:")
print([f for f in os.listdir(path) if os.path.isfile(os.path.join(path, f))])

# List everything
print("\nAll Directories and Files:")
print(os.listdir(path))
