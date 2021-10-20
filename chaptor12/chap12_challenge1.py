class Rectangle:
    def __init__(self, width, length):
        self.width = width
        self.length = length

    def calculate_perimeter(self):
        return (self.width + self.length) * 2

class Square:
    def __init__(self, shape):
        self.shape = shape

    def calculate_perimeter(self):
        return self.shape * 4
        
rectangle = Rectangle(2, 3)
print(rectangle.calculate_perimeter())

square = Square(4)
print(square.calculate_perimeter())