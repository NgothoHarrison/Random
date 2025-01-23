# Multiple Inheritance is a feature of some object-oriented computer programming languages in which
#  a class can inherit attributes and methods from more than one parent class.

# multi-level inheritance
# this is where a class inherits from a class that inherits from another class
# the class at the top of the hierarchy is called the super class

# super class
class Animal:

    def __init__(self, name): # constructor, or the initializer
        self.name = name


    def eat(self):
        print(f"This {self.name} is eating")

    def sleep(self):
        print(f"This {self.name} is sleeping")


# multiple parent classes here
class Prey(Animal): 
    def flee(self):
        print(f"This {self.name} is fleeing")

class Predator(Animal):
    def hunt(self):
        print(f"{self.name} is hunting")

# now the child classes here
class Rabbit(Prey):
    pass

class Hawk(Predator):
    pass

class Fish(Prey, Predator): # multiple inheritance from multiple parents
    pass


rabbit = Rabbit("Tonny the Rabbit")
hawk = Hawk("Nimo the Hawk")
fish = Fish("Yutu the Fish")

rabbit.flee()
fish.hunt()
fish.flee()
rabbit.eat()