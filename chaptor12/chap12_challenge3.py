from warnings import showwarning


class Shape:
    def what_am_i(self):
        print("I am a shape")

class Rectangle(Shape):
    def __init__(self, width, length):
        self.width = width
        self.length = length

    def calculate_perimeter(self):
        return (self.width + self.length) * 2

class Square(Shape):
    def __init__(self, shape):
        self.shape = shape

    def calculate_perimeter(self):
        return self.shape * 4

a_rectangle = Rectangle(10, 20)
a_rectangle.what_am_i()

a_square = Square(10)
a_square.what_am_i()