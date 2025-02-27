#Read in a Fahrenheit temperature. 
#Calculate and display the equivalent centigrade temperature. 
#The following formula is used for the conversion:
#C = (5 / 9) * (F – 32)

def celsius(farenheit):
    return (5 / 9) * (farenheit-32)
    
farenheit = int(input())
res = celsius(farenheit)
print(res)