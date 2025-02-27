# 2. Define a class named Shape and its subclass Square.
# The Square class has an init function which takes a length as argument.
# Both classes have a area function which can print the area of the shape where Shape's area is 0 by default.

class Shape:
    def __init__(self):
        self.area_value = 0  

    def area(self):
        print(f"Area: {self.area_value}")


class Square(Shape):
    def __init__(self, length):
        super().__init__()  
        self.length = length
        self.area_value = length ** 2  

    def area(self):
        print(f"Area of square: {self.area_value}")


shape = Shape()
shape.area() 

square = Square(int(input()))
square.area()