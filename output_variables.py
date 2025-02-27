x = "Python is awesome"
print(x)

#Python is awesome

x = "Python"
y = "is"
z = "awesome"
print(x, y, z)

#Python is awesome

x = "Python "
y = "is "
z = "awesome"
print(x + y + z)

#Python is awesome
#Обратите внимание на пробел после "Python " и "is ", без них результат будет "Pythonisawesome".

x = 5
y = 10
print(x + y)

#15

#В функции print(), если вы пытаетесь объединить строку и число с помощью оператора +, Python выдаст ошибку:
#x = 5
#y = "John"
#print(x + y)

x = 5
y = "John"
print(x, y)

#5 John