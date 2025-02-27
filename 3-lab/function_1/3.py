#Write a program to solve a classic puzzle: 
#We count 35 heads and 94 legs among the chickens and rabbits in a farm. 
#How many rabbits and how many chickens do we have?
#create function: solve(numheads, numlegs):

# a = chicken b = rabbit
# a + b = numheads.       a = numheads - b
# 2a + 4b = numlegs.      2(numheads - b) + 4b = numlegs
# 2numheads + 2b = numlegs
# 2b = numlegs - 2numheads
# b = ((numlegs) / 2) - numheads

def solve(numheads, numlegs):
    b = ((numlegs) / 2) - numheads
    a = numheads - b
    return a, b
numheads = 35
numlegs = 94
res = solve(numheads, numlegs)
print(res)