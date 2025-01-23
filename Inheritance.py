# Inheritance is a way to form new classes using classes that have already been defined. 
# The newly formed classes are called derived classes, the classes that we derive from 
# are called base classes. 
# Important benefits of inheritance are code reuse and reduction of complexity of a program. 
# The derived classes (descendants) override or extend the functionality of base classes (ancestors).

class Animal: # base class, or the parent class, or the superclass

    def __init__(self, name):
        self.name = name # instance variable or the attribute of the class 
        self.is_alive = True

    def eat(self):
        print(f'{self.name} is eating')

    def sleep(self):
        print(f'{self.name} is sleeping')

    def breathe(self):
        print(f'{self.name} is breathing')

    def alive(self):
        if self.is_alive:
            print(f'{self.name} is alive')
        else:
            print(f'{self.name} is dead')

class Dog(Animal): # derived class, or the child class, or the subclass
    def bark(self):
        print(f'{self.name} is barking')

class Cat(Animal): # derived class, or the child class, or the subclass
    def meow(self):
        print(f'{self.name} is meowing')

class Mammal(Animal): # derived class, or the child class, or the subclass

    def __init__(self, name, species):
        super().__init__(name)
        self.species = species

    def give_birth(self):
        print(f'{self.name} is giving birth')

    def feed_young(self):
        print(f'{self.name} is feeding its young')

dog = Dog("Bosco")
cat = Cat("Mittens")
mammal = Mammal("Lion", "Human")

print(dog.name, cat.name)
print (dog.eat(), cat.sleep())
print(dog.alive(), cat.alive())
print(dog.bark(), cat.meow())
print(f"{mammal.give_birth()} ") # this will is called from the Mammal class