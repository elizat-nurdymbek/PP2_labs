#A set is a collection which is unordered, unchangeable*, and unindexed.
#Note: Set items are unchangeable, but you can remove items and add new items.
thisset = {"apple", "banana", "cherry"}
print(thisset)     #{'cherry', 'apple', 'banana'}
# Note: the set list is unordered, meaning: the items will appear in a random order.
# Refresh this page to see the change in the result.

#Once a set is created, you cannot change its items, but you can remove items and add new items.

thisset = {"apple", "banana", "cherry", "apple"}
print(thisset)      #{'banana', 'cherry', 'apple'}

#Note: The values True and 1 are considered the same value in sets, and are treated as duplicates:
thisset = {"apple", "banana", "cherry", True, 1, 2}
print(thisset)      #True, 2, 'banana', 'cherry', 'apple'}

#Note: The values False and 0 are considered the same value in sets, and are treated as duplicates:
thisset = {"apple", "banana", "cherry", False, True, 0}
print(thisset)      #{False, True, 'cherry', 'apple', 'banana'}

thisset = set(("apple", "banana", "cherry"))
print(thisset)      #{'apple', 'cherry', 'banana'}
# Note: the set list is unordered, so the result will display the items in a random order.



                #ADD SET ITEMS
#To add one item to a set use the add() method.
thisset = {"apple", "banana", "cherry"}
thisset.add("orange")
print(thisset)         #{'banana', 'cherry', 'orange', 'apple'}

 #To add items from another set into the current set, use the update() method.
thisset = {"apple", "banana", "cherry"}
tropical = {"pineapple", "mango", "papaya"}
thisset.update(tropical)
print(thisset)            #{'apple', 'mango', 'cherry', 'pineapple', 'banana', 'papaya'}

#The object in the update() method does not have to be a set, it can be any iterable object (tuples, lists, dictionaries etc.).
thisset = {"apple", "banana", "cherry"}
mylist = ["kiwi", "orange"]
thisset.update(mylist)
print(thisset)             #{'banana', 'cherry', 'apple', 'orange', 'kiwi'}



                #REMOVE SET ITEMS
#To remove an item in a set, use the remove(), or the discard() method.
thisset = {"apple", "banana", "cherry"}
thisset.remove("banana")
print(thisset)       #{'cherry', 'apple'}

#Note: If the item to remove does not exist, remove() will raise an error.

thisset = {"apple", "banana", "cherry"}
thisset.discard("banana")
print(thisset)        #{'cherry', 'apple'}

#Note: If the item to remove does not exist, discard() will NOT raise an error.

#You can also use the pop() method to remove an item, but this method will remove a random item, so you cannot be sure what item that gets removed.
#The return value of the pop() method is the removed item.
thisset = {"apple", "banana", "cherry"}
x = thisset.pop()
print(x) #removed item                     #cherry
print(thisset) #the set after removal      #{'apple', 'banana'}

#Note: Sets are unordered, so when using the pop() method, you do not know which item that gets removed.

thisset = {"apple", "banana", "cherry"}
thisset.clear()
print(thisset)              #set()
 
thisset = {"apple", "banana", "cherry"}
del thisset
print(thisset) #this will raise an error because the set no longer exists




               #LOOP SETS
thisset = {"apple", "banana", "cherry"}

for x in thisset:
  print(x)
#banana
#cherry
#apple



               #JOIN SETS
#The union() and update() methods joins all items from both sets.

#The intersection() method keeps ONLY the duplicates.

#The difference() method keeps the items from the first set that are not in the other set(s).

#The symmetric_difference() method keeps all items EXCEPT the duplicates.
               
#The union() method returns a new set with all items from both sets.
set1 = {"a", "b", "c"}
set2 = {1, 2, 3}

set3 = set1.union(set2)
print(set3)                #{'c', 1, 'b', 'a', 3, 2}

#You can use the | operator instead of the union() method, and you will get the same result.
set1 = {"a", "b", "c"}
set2 = {1, 2, 3}

set3 = set1 | set2
print(set3)               #{1, 'b', 'c', 'a', 2, 3}

#All the joining methods and operators can be used to join multiple sets.
set1 = {"a", "b", "c"}
set2 = {1, 2, 3}
set3 = {"John", "Elena"}
set4 = {"apple", "bananas", "cherry"}

myset = set1.union(set2, set3, set4)
print(myset)                 #{banana, apple, 'a', cherry, 'c', 2, Elena, 3, 'b', John, 1}

#When using the | operator, separate the sets with more | operators:
set1 = {"a", "b", "c"}
set2 = {1, 2, 3}
set3 = {"John", "Elena"}
set4 = {"apple", "bananas", "cherry"}

myset = set1 | set2 | set3 |set4
print(myset)                    #{apple, banana, 'a', 1, 'b', 2, Elena, John, 'c', 3, cherry}

#The union() method allows you to join a set with other data types, like lists or tuples.
x = {"a", "b", "c"}
y = (1, 2, 3)

z = x.union(y)
print(z)                    #{1, 'b', 'a', 2, 'c', 3}

#Note: The  | operator only allows you to join sets with sets, and not with other data types like you can with the  union() method.

#The update() method inserts all items from one set into another.
#set1 = {"a", "b", "c"}
set2 = {1, 2, 3}

set1.update(set2)
print(set1)             #{'b', 2, 'a', 'c', 3, 1}

#Note: Both union() and update() will exclude any duplicate items.

#The intersection() method will return a new set, that only contains the items that are present in both sets.
set1 = {"apple", "banana", "cherry"}
set2 = {"google", "microsoft", "apple"}

set3 = set1.intersection(set2)
print(set3)                         #{'apple'}

#You can use the & operator instead of the intersection() method, and you will get the same result.
set1 = {"apple", "banana" , "cherry"}
set2 = {"google", "microsoft", "apple"}

set3 = set1 & set2
print(set3)                     #{'apple'}

#Note: The & operator only allows you to join sets with sets, and not with other data types like you can with the intersection() method.

#The intersection_update() method will also keep ONLY the duplicates, but it will change the original set instead of returning a new set.
set1 = {"apple", "banana", "cherry"}
set2 = {"google", "microsoft", "apple"}

set1.intersection_update(set2)
print(set1)                    #{'apple'}

#The values True and 1 are considered the same value. The same goes for False and 0.
set1 = {"apple", 1, "banana", 0, "cherry"}
set2 = {False, "google", "microsoft", "apple", True}

set3 = set1.intersection(set2)
print(set3)                       #{False, True, 'apple'}

#The difference() method will return a new set that will contain only the items from the first set that are not present in the other set.
set1 = {"apple", "banana" , "cherry"}
set2 = {"google", "microsoft", "apple"}

set3 = set1.difference(set2)
print(set3)                       #{'banana', 'cherry'}

set1 = {"apple", "banana" , "cherry"}
set2 = {"google", "microsoft", "apple"}

set3 = set1 - set2
print(set3)                       #{'banana', 'cherry'}

#Note: The - operator only allows you to join sets with sets, and not with other data types like you can with the difference() method.

#The difference_update() method will also keep the items from the first set that are not in the other set, but it will change the original set instead of returning a new set.
set1 = {"apple", "banana" , "cherry"}
set2 = {"google", "microsoft", "apple"}

set1.difference_update(set2)
print(set1)                       #{'banana', 'cherry'}

#The symmetric_difference() method will keep only the elements that are NOT present in both sets.
set1 = {"apple", "banana" , "cherry"}
set2 = {"google", "microsoft", "apple"}

set3 = set1.symmetric_difference(set2)
print(set3)                  #{'google', 'banana', 'microsoft', 'cherry'}

#You can use the ^ operator instead of the symmetric_difference() method, and you will get the same result.
set1 = {"apple", "banana", "cherry"}
set2 = {"google", "microsoft", "apple"}

set3 = set1 ^ set2

print(set3)                    #{'google', 'banana', 'microsoft', 'cherry'}

#Note: The ^ operator only allows you to join sets with sets, and not with other data types like you can with the symmetric_difference() method.

#The symmetric_difference_update() method will also keep all but the duplicates, but it will change the original set instead of returning a new set.
set1 = {"apple", "banana" , "cherry"}
set2 = {"google", "microsoft", "apple"}

set1.symmetric_difference_update(set2)
print(set1)                       #{'google', 'banana', 'microsoft', 'cherry'}




                     #SET METHODS
#add()                      Adds an element to the set
#clear()                      Removes all the elements from the set
#copy()                          Returns a copy of the set
#difference()         -        Returns a set containing the difference between two or more sets
#difference_update() -=        Removes the items in this set that are also included in another, specified set
#discard()                      Remove the specified item
#intersection()         &        Returns a set, that is the intersection of two other sets
#intersection_update() &=        Removes the items in this set that are not present in other, specified set(s)
#isdisjoint()                  Returns whether two sets have a intersection or not
#issubset()             <=        Returns whether another set contains this set or not
#                      <        Returns whether all items in this set is present in other, specified set(s)
#issuperset()         >=        Returns whether this set contains another set or not
#                      >        Returns whether all items in other, specified set(s) is present in this set
#pop()                          Removes an element from the set
#remove()                      Removes the specified element
#symmetric_difference() ^        Returns a set with the symmetric differences of two sets
#symmetric_difference_update() ^= Inserts the symmetric differences from this set and another
#union()             |        Return a set containing the union of sets
#update()             |=        Update the set with the union of this set and others