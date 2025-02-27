# 4. Write the definition of a Point class. Objects from this class should have a
#    - a method show to display the coordinates of the point
#    - a method move to change these coordinates
#    - a method dist that computes the distance between 2 points

import math

class Point:
    def __init__(self, x, y):
        self.x = x
        self.y = y
    
    def show(self):
        print(f"Point coordinates: ({self.x}, {self.y})")
    
    def move(self, new_x, new_y):
        self.x = new_x
        self.y = new_y
    
    def dist(self, other_point):
        return math.sqrt((self.x - other_point.x) ** 2 + (self.y - other_point.y) ** 2) 

x1, y1 = map(int, input("Введите координаты точки p1 (x y): ").split())
p1 = Point(x1, y1)

x2, y2 = map(int, input("Введите координаты точки p2 (x y): ").split())
p2 = Point(x2, y2)

p1.show()
p2.show()

distance = p1.dist(p2)
print(f"Расстояние между точками: {distance}")