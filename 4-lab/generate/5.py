def countdown(n):
    while n >= 0:
        yield n
        n -= 1

n = int(input("Enter a number to countdown from: "))
for i in countdown(n):
    print(i, end=" ")
