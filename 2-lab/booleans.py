# True # False
print(10 > 9) #True
print(10 == 9) #False
print(10 < 9) #False

a = 200
b = 33
if b > a:
  print("b is greater than a")
else:
  print("b is not greater than a") #b is not greater than a
  
print(bool("Hello")) #True
print(bool(15)) #True

x = "Hello"
y = 15

print(bool(x)) #True
print(bool(y)) #True

#Any string, number, list is True, except 0 and empty

print(bool("abc")) #True
print(bool(123)) #True
print(bool(["apple", "cherry", "banana"])) #True

bool(False) #False
bool(None) #False
bool(0) #False
bool("") #False
bool(()) #False
bool([]) #False
bool({}) #False

#Еще одно значение или объект, в данном случае, оценивается как False. Это происходит, если у вас есть объект, созданный из класса с функцией len, которая возвращает 0 или False.
class myclass():
  def __len__(self):
    return 0
myobj = myclass()
print(bool(myobj)) #False

def myFunction() :
  return True
print(myFunction()) #True

def myFunction() :
  return True
if myFunction():
  print("YES!")
else:
  print("NO!") #YES!

#В Python также есть множество встроенных функций, которые возвращают булево значение, например, функция 
#isinstance(), которую можно использовать для определения, принадлежит ли объект определенному типу данных.

x = 200
print(isinstance(x, int)) #True