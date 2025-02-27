#int x=1
#float y=2.8
#complex z=1j

#Convert from one type to another:
x = 1    # int
y = 2.8  # float
z = 1j   # complex

#convert from int to float:
a = float(x)
#convert from float to int:
b = int(y)
#convert from int to complex:
c = complex(x)

print(a)
print(b)
print(c)

print(type(a))
print(type(b))
print(type(c))

#1.0
#2
#(1+0j)
#<class 'float'>
#<class 'int'>
#<class 'complex'>

#Примечание: Нельзя преобразовать комплексные числа в другой тип чисел.

#В Python нет функции random() для генерации случайных чисел, но существует встроенный модуль random, который можно использовать для создания случайных чисел:

#Import the random module, and display a random number between 1 and 9:
import random

print(random.randrange(1, 10))