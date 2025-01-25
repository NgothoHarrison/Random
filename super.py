#  super() = function used in a child class to call methods from a parent class(superclass)
# Allows you to extend the functionality of the inherited methods

class Shape:     # The super class
    def __init__(self, color, is_filled):
        self.color = color
        self.is_filled = is_filled

    def describe(self):
        print(f"It is {self.color} and {"filled " if self.is_filled else "not filled"}")

class Circle(Shape):
    def __init__(self, color, is_filled, radius):
        super().__init__( color, is_filled)
        # self.color = color   we replace these that are repeated across multiple child classes
        # self.filled = filled
        self.radius = radius

class Square(Shape):
    def __init__(self, color, is_filled, width):
        super().__init__( color, is_filled)
        self.width = width

class Triangle(Shape):
    def __init__(self, color, is_filled,width, height):
        super().__init__(color, is_filled)
        self.width = width
        self.height = height

# objects
circle = Circle( color="red", is_filled=True, radius=26 )
square = Square( 'blue', False, 67)

print(circle.color)
print(square.color)
print(f"{square.width} cm")

circle.describe()
square.describe()