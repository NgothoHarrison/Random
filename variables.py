# class variables are variables that are shared among all instances of a class
# instance variables are unique to each instance of a class
# class variables are defined outside of any methods in a class
# they allow you to share data among all instances of a class

class Student:
    # class variables
    school = 'Moringa School'
    location = 'Nairobi'
    number_of_students = 0

    def __init__(self, name, age, major):
        self.name = name
        self.age = age
        self.major = major
        Student.number_of_students += 1 # increment the number of students by 1

student1 = Student('John', 20, 'Computer Science')
student2 = Student('Jane', 21, 'Information Technology')
student3 = Student('Doe', 22, 'Software Engineering')

print(f"{student1.name}  is at { student1.school}")
print(student2.age)
print(student3.major)

print(f"""my graduating class of {student1.major} is at {student1.location}
       from {Student.school} and are {Student.number_of_students} students""")