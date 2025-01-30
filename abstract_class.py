#  Abstract class is a class that is designed to be specifically used as a base class.
#  An abstract class is a class that cannot be instantiated on its own and is designed to be
#  inherited by other classes.
# thus, abstract classes are used to define a blueprint for other classes.
# basically a blueprint

from abc import ABC, abstractmethod

class Vehicle(ABC):

    @abstractmethod
    def go(self):
        pass

    @abstractmethod
    def stop(self):
        pass

class Car(Vehicle):
    
    def go(self):
        print("You drive the car")

    def stop(self):
        print("You stop the car")

class Nduthi(Vehicle):
    def go(self):
        print("You ride a motorcycle")

    def stop(self):
        print("You stop the motorcycle")


motorcycle = Nduthi()
car = Car()

motorcycle.go()
motorcycle.stop()

car.go()
car.stop()