#Error
#age = 36
#txt = "My name is John, I am " + age
#print(txt)

#But we can combine strings and numbers by using f-strings or the format() method!
#To specify a string as an f-string, simply put an f in front of the string literal, and add curly brackets {} as placeholders for variables and other operations.

age = 36
txt = f"My name is John, I am {age}"
print(txt) #My name is John, I am 36

#Add a placeholder for the price variable:
price = 59 
txt = f"The price is {price} dollars" 
print(txt) #The price is 59 dollars

#Заполнитель может включать модификатор для форматирования значения.

#Модификатор добавляется через двоеточие : после плейсхолдера, за которым следует тип форматирования, например, .2f, что означает число с фиксированной точкой и 2 знаками после запятой.

#Display the price with 2 decimals:
price = 59 
txt = f"The price is {price:.2f} dollars" 
print(txt) #The price is 59.00 dollars

#Perform a math operation in the placeholder, and return the result:
txt = f"The price is {20 * 59} dollars" 
print(txt) #The price is 1180 dollars