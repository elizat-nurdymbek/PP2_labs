# You are given list of numbers separated by spaces. 
# Write a function filter_prime which will take list of numbers as 
# an agrument and returns only prime numbers from the list.

def prime_san(a):
    if a < 2:
        return False
    for i in range(2, a):
        if a % i == 0:
            return False
    return True

def filter_prime(numbers):
    return [num for num in numbers if prime_san(num)]

numbers = (map(int, input("Sandi engiz: ").split()))
prime_numbers = filter_prime(numbers)
print(f"Prime numbers: {prime_numbers}")