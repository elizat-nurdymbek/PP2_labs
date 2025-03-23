from functools import reduce

def multiply_list(numbers):
    return reduce(lambda x, y: x * y, numbers)

nums = list(map(int, input().split()))
print(multiply_list(nums))