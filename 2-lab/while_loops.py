# With the while loop we can execute a set of statements as long as a condition is true.
i = 1
while i < 6:
  print(i)
  i += 1
# 1
# 2
# 3
# 4
# 5

# Note: remember to increment i, or else the loop will continue forever.

# The while loop requires relevant variables to be ready, in this example we need to define an indexing variable, i, which we set to 1.

i = 1
while i < 6:
  print(i)
  if (i == 3):
    break
  i += 1
# 1
# 2
# 3

i = 0
while i < 6:
  i += 1
  if i == 3:
    continue
  print(i)
# Note that number 3 is missing in the result
# 1
# 2
# 3
# 4
# 5
# 6

i = 1
while i < 6:
  print(i)
  i += 1
else:
  print("i is no longer less than 6")
# 1
# 2
# 3
# 4
# 5
# i is no longer less than 6