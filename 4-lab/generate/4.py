def squares(a, b):
    for i in range(a, b + 1):
        yield i ** 2

a = int(input("Enter the start of the range (a): "))
b = int(input("Enter the end of the range (b): "))
for i in squares(a, b):
    print(i, end=" ")