thistuple = ("apple", "banana", "cherry")
print(thistuple)   #('apple', 'banana', 'cherry')

thistuple = ("apple",)
print(type(thistuple))    #<class 'tuple'>

#NOT a tuple
thistuple = ("apple")
print(type(thistuple))     #<class 'str'>

#It is also possible to use the tuple() constructor to make a tuple.
thistuple = tuple(("apple", "banana", "cherry"))
print(thistuple)      #('apple', 'banana', 'cherry')



                  #UPDATE TUPLES
#Once a tuple is created, you cannot change its values. Tuples are unchangeable, or immutable as it also is called.
x = ("apple", "banana", "cherry")
y = list(x)
y[1] = "kiwi"
x = tuple(y)
print(x)          #("apple", "kiwi", "cherry")

#Since tuples are immutable, they do not have a built-in append() method, but there are other ways to add items to a tuple.
#1. Convert into a list: Just like the workaround for changing a tuple, you can convert it into a list, add your item(s), and convert it back into a tuple.
thistuple = ("apple", "banana", "cherry")
y = list(thistuple)
y.append("orange")
thistuple = tuple(y)
print(thistuple)       #('apple', 'banana', 'cherry', 'orange')

#2. Add tuple to a tuple. You are allowed to add tuples to tuples, so if you want to add one item, (or many), create a new tuple with the item(s), and add it to the existing tuple:
thistuple = ("apple", "banana", "cherry")
y = ("orange",)
thistuple += y
print(thistuple)     #('apple', 'banana', 'cherry', 'orange')

#Note: When creating a tuple with only one item, remember to include a comma after the item, otherwise it will not be identified as a tuple.

#Note: You cannot remove items in a tuple.

#Tuples are unchangeable, so you cannot remove items from it, but you can use the same workaround as we used for changing and adding tuple items:
thistuple = ("apple", "banana", "cherry")
y = list(thistuple)
y.remove("apple")
thistuple = tuple(y)
print(thistuple)       #('banana', 'cherry')

thistuple = ("apple", "banana", "cherry")
del thistuple
print(thistuple) #this will raise an error because the tuple no longer exists




               #UNPACK TUPLES
fruits = ("apple", "banana", "cherry")
(green, yellow, red) = fruits
print(green)
print(yellow)
print(red)
#apple
#banana
#cherry

#Note: The number of variables must match the number of values in the tuple, if not, you must use an asterisk to collect the remaining values as a list.

#If the number of variables is less than the number of values, you can add an * to the variable name and the values will be assigned to the variable as a list:
fruits = ("apple", "banana", "cherry", "strawberry", "raspberry")
(green, yellow, *red) = fruits
print(green)
print(yellow)
print(red)
#apple
#banana
#['cherry', 'strawberry', 'raspberry']

fruits = ("apple", "mango", "papaya", "pineapple", "cherry")
(green, *tropic, red) = fruits
print(green)
print(tropic)
print(red)
#apple
#['mango', 'papaya', 'pineapple']
#cherry




                    #LOOP TUPLES
thistuple = ("apple", "banana", "cherry")
for x in thistuple:
  print(x)
#apple
#banana
#cherry

#Use the range() and len() functions to create a suitable iterable.
thistuple = ("apple", "banana", "cherry")
for i in range(len(thistuple)):
  print(thistuple[i])
#apple
#banana
#cherry

thistuple = ("apple", "banana", "cherry")
i = 0
while i < len(thistuple):
  print(thistuple[i])
  i = i + 1
#apple
#banana
#cherry



                   #JOIN TUPLES
tuple1 = ("a", "b" , "c")
tuple2 = (1, 2, 3)
tuple3 = tuple1 + tuple2
print(tuple3)         #('a', 'b', 'c', 1, 2, 3)

fruits = ("apple", "banana", "cherry")
mytuple = fruits * 2
print(mytuple)        #('apple', 'banana', 'cherry', 'apple', 'banana', 'cherry')


 
               #TUPLE METHODS
#count() Returns the number of times a specified value occurs in a tuple
#index() Searches the tuple for a specified value and returns the position of where it was found