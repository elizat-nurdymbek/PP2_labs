# 3. Define a class named Rectangle which inherits from Shape class from task 2.
# Class instance can be constructed by a length and width.
# The Rectangle class has a method which can compute the area.

class Shape:
    def __init__(self):
        self.area_value = 0 

    def area(self):
        print(f"Area: {self.area_value}")


class Rectangle(Shape):
    def __init__(self, length, width):
        super().__init__() 
        self.length = length
        self.width = width
        self.area_value = length * width  

    def area(self):
        print(f"Area of rectangle: {self.area_value}")


length, width = map(int, input("Enter length and width: ").split())  
rect = Rectangle(length, width)
rect.area()