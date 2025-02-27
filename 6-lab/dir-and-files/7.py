source_file = input("Enter the source file path: ")
destination_file = input("Enter the destination file path: ")

with open(source_file, 'r') as src, open(destination_file, 'w') as dest:
    dest.write(src.read())

print(f"Copied content from {source_file} to {destination_file}")
