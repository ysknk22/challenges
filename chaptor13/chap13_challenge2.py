class Shape:
    def what_am_i(self):
        print("I am a shape")

class Square(Shape):
    square_list = []

    def __init__(self, shape):
        self.shape = shape
        self.square_list.append(self)

    def calculate_perimeter(self):
        return self.shape * 4

    def what_am_i(self):
        super().what_am_i()
        print("I am a Square.")

    def __repr__(self):
        return "{} by {} by {} by {}".format(self.shape, self.shape, self.shape, self.shape)

a_square = Square(10)
print(a_square)
