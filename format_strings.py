# A function is a block of code which only runs when it is called.
# You can pass data, known as parameters, into a function.
# A function can return data as a result.

def my_function():
  print("Hello from a function")

my_function()
# Hello from a function

# Information can be passed into functions as arguments.
# Arguments are specified after the function name, inside the parentheses. You can add as many arguments as you want, just separate them with a comma.
# The following example has a function with one argument (fname). When the function is called, we pass along a first name, which is used inside the function to print the full name:

def my_function(fname):
  print(fname + " Refsnes")

my_function("Emil")
my_function("Tobias")
my_function("Linus")
# Emil Refsnes
# Tobias Refsnes
# Linus Refsnes

# Arguments are often shortened to args in Python documentations.

# The terms parameter and argument can be used for the same thing: information that are passed into a function.

# From a function's perspective:
# A parameter is the variable listed inside the parentheses in the function definition.
# An argument is the value that is sent to the function when it is called.

def my_function(fname, lname):
  print(fname + " " + lname)
my_function("Emil", "Refsnes")
# Emil Refsnes

def my_function(fname, lname):
  print(fname + " " + lname)
my_function("Emil")

# If you do not know how many arguments that will be passed into your function, add a * before the parameter name in the function definition.
def my_function(*kids):
  print("The youngest child is " + kids[2])
my_function("Emil", "Tobias", "Linus")
# The youngest child is Linus

def my_function(*kids):
  print("The youngest child is " + kids[2])
my_function("Emil", "Tobias", "Linus")
# The youngest child is Linus

# Arbitrary Arguments are often shortened to *args in Python documentations.

# You can also send arguments with the key = value syntax.
# This way the order of the arguments does not matter.

def my_function(child3, child2, child1):
  print("The youngest child is " + child3)
my_function(child1 = "Emil", child2 = "Tobias", child3 = "Linus")
# The youngest child is Linus

# The phrase Keyword Arguments are often shortened to kwargs in Python documentations.

# If you do not know how many keyword arguments that will be passed into your function, add two asterisk: ** before the parameter name in the function definition.

# If the number of keyword arguments is unknown, add a double ** before the parameter name:
def my_function(**kid):
  print("His last name is " + kid["lname"])
my_function(fname = "Tobias", lname = "Refsnes")
# His last name is Refsnes

# Arbitrary Kword Arguments are often shortened to **kwargs in Python documentations.

# If we call the function without argument, it uses the default value:
def my_function(country = "Norway"):
  print("I am from " + country)
my_function("Sweden")
my_function("India")
my_function()
my_function("Brazil")
# I am from Sweden
# I am from India
# I am from Norway
# I am from Brazil

# You can send any data types of argument to a function (string, number, list, dictionary etc.), and it will be treated as the same data type inside the function.
def my_function(food):
  for x in food:
    print(x)
fruits = ["apple", "banana", "cherry"]
my_function(fruits)
# apple
# banana
# cherry

def my_function(x):
  return 5 * x
print(my_function(3))
print(my_function(5))
print(my_function(9))
# 15
# 25
# 45

# function definitions cannot be empty, but if you for some reason have a function definition with no content, put in the pass statement to avoid getting an error.
def myfunction():
  pass
# having an empty function definition like this, would raise an error without the pass statement

# You can specify that a function can have ONLY positional arguments, or ONLY keyword arguments.
# To specify that a function can have only positional arguments, add , / after the arguments:

def my_function(x, /):
  print(x)
my_function(3)
# 3

# Without the , / you are actually allowed to use keyword arguments even if the function expects positional arguments:
def my_function(x):
  print(x)
my_function(x = 3)
# 3

# But when adding the , / you will get an error if you try to send a keyword argument:
def my_function(x, /):
  print(x)
my_function(x = 3)

# To specify that a function can have only keyword arguments, add *, before the arguments:
def my_function(*, x):
  print(x)
my_function(x = 3)
# 3

# Without the *, you are allowed to use positionale arguments even if the function expects keyword arguments:
def my_function(x):
  print(x)
my_function(3)
# 3

# But with the *, you will get an error if you try to send a positional argument:
def my_function(*, x):
  print(x)
my_function(3)

# Any argument before the / , are positional-only, and any argument after the *, are keyword-only.
def my_function(a, b, /, *, c, d):
  print(a + b + c + d)
my_function(5, 6, c = 7, d = 8)
# 26 

# The developer should be very careful with recursion as it can be quite easy to slip into writing a function which never terminates, or one that uses excess amounts of memory or processor power. However, when written correctly recursion can be a very efficient and mathematically-elegant approach to programming.
# In this example, tri_recursion() is a function that we have defined to call itself ("recurse"). We use the k variable as the data, which decrements (-1) every time we recurse. The recursion ends when the condition is not greater than 0 (i.e. when it is 0).
# To a new developer it can take some time to work out how exactly this works, best way to find out is by testing and modifying it.

def tri_recursion(k):
  if(k > 0):
    result = k + tri_recursion(k - 1)
    print(result)
  else:
    result = 0
  return result
print("Recursion Example Results:")
tri_recursion(6)
# Recursion Example Results:
# 1
# 3
# 6
# 10
# 15
# 21