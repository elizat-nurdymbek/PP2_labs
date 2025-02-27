# Write a function that computes the volume of a sphere given its radius

import math

def sphere(radius):
    return (4/3) * math.pi * (radius ** 3)

r = float(input("Radius of the sphere: "))
print("Volume of the sphere:", sphere(r))