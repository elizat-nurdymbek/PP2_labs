# Write a function that takes in a list of integers and returns True if it contains 007 in order
# def spy_game(nums):
#    pass
# spy_game([1,2,4,0,0,7,5]) --> True
# spy_game([1,0,2,4,0,5,7]) --> True
# spy_game([1,7,2,0,4,5,0]) --> False

def spy_game(nums):
    code = [0, 0, 7]

    for num in nums:
        if num == code[0]: 
            code.pop(0)
        if not code:
            return True

    return False

sandar = list(map(int, input().split()))
print(spy_game(sandar))