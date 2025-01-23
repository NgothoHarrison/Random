# This is the class that we are using to represent a car

class Car:
    def __init__(self, make, model, color, year, for_sale):
        self.make = make
        self.model = model
        self.color = color
        self.year = year
        self.for_sale = for_sale

# method = a function that is associated with a class

    def start(self):
        print(f'You have {self.make} {self.model} and is now starting')

    def drive(self):
        print(f'You are now driving {self.make} {self.model} and is {self.for_sale}')

    def stop(self):
        print(f'You have stopped {self.make} {self.model}')

    def details(self):
        print(f'You have a {self.year} {self.make} {self.model} in {self.color} color')