#  super() = function used in a child class to call methods from a parent class(superclass)
# Allows you to extend the functionality of the inherited methods

class Shape:     # The super class
    def __init__(self, color, filled):
        self.color = color
        self.filled = filled

class Circle(Shape):
    def __init__(self, color, filled, radius):
        self.color = color
        self.filled = filled
        self.radius = radius

class Square(Shape):
