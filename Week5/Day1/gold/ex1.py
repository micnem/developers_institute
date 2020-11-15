import math
class Circle:
    def __init__(self, radius = 1.0):
        self.radius = radius
    def perimiter(self):
        print(f"The perimeter of circle with radius {self.radius} is {2*math.pi*self.radius}")
    def area(self):
        print(f"The area of a circle with radius {self.radius} is {math.pi * (self.radius ** 2)}")
    def definition(self):
        print("The definition of a circle is a shape where all points are equidistant from the centre.")

circ = Circle(13)
circ.perimiter()
circ.area()
circ.definition()