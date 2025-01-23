# object = a bundle of related attributes (variables) and methods (functions)
# a class = a blueprint for creating objects
from car import Car # this is importation of the class file

car1 = Car('Toyota', 'vitz', 'red', 2020, True)
car2 = Car('Ford', 'Fiesta', 'blue', 2019, False)
car3 = Car('Honda', 'Civic', 'black', 2018, True)


car1.start()
car1.drive()
car2.stop()
car3.details()

