def countdown(n):
    while n >= 0.3:
        yield round(n, 1)
        n -= 0.1

n = float(input("Enter a number to countdown from: "))
for i in countdown(n):
    print(i, end=" ")