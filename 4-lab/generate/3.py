def divisible_by_3_and_4(n):
    for i in range(n + 1):
        if i % 3 == 0 and i % 4 == 0:
            yield i

n = int(input("Enter a number to get numbers divisible by 3 and 4: "))
for i in divisible_by_3_and_4(n):
    print(i, end=" ")