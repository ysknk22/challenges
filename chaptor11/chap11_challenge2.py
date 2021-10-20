import math
from os import pipe

class Circle():
    def __init__(self, radius):
        self.radius = radius

    def area(self):
        return self.radius ** 2 * math.pi

circle = Circle(10)
print(circle.area())