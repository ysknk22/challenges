class Square:
    def __init__(self, shape):
        self.shape = shape

    def calculate_perimeter(self):
        return self.shape * 4

    def change_size(self, new_size):
        self.shape += new_size

square = Square(100)
print(square.shape)

square.change_size(200)
print(square.shape)