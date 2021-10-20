class Horse:
    def __init__(self, weight, name, rider):
        self.weight = weight
        self.name = name
        self.rider = rider

class Rider:
    def __init__(self, height, weight, name):
        self.height = height
        self.weight = weight
        self.name = name

yutaka = Rider(170, 50, "Yutaka Take")
kitasanblack = Horse(543, "Kitasanblack", yutaka)

print("The name of Horse is {}".format(kitasanblack.name))
print("The name of Rider is {}".format(kitasanblack.rider.name))