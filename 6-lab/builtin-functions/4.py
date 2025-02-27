import time
import math

def delayed_sqrt(number, delay_ms):
    time.sleep(delay_ms / 1000)  #milliseconds -> seconds
    return math.sqrt(number)

number = int(input("Enter the number: "))
delay_ms = int(input("Enter the delay in milliseconds: "))

result = delayed_sqrt(number, delay_ms)
print(f"Square root of {number} after {delay_ms} milliseconds is {result}")
