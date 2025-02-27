# 6. Write a program which can filter prime numbers in a list by using filter function.
# Note: Use lambda to define anonymous functions.

def is_prime(n):
    if n < 2:
        return False
    for i in range(2, int(n ** 0.5) + 1):
        if n % i == 0:
            return False
    return True

numbers = [10, 15, 3, 7, 19, 23, 8, 4, 31]

prime_numbers = list(filter(lambda x: is_prime(x), numbers))

print("Prime numbers:", prime_numbers)