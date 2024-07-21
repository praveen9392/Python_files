class Person:
    def role(self):
        print("This is a general person")

class Student(Person):
    def role(self):
        print("He is treated as a student at college or school")

class Son(Person):
    def role(self):
        print("He is treated as a son at home")

class Employee(Person):
    def role(self):
        print("He is treated as an employee at the office")

# Function to demonstrate polymorphism
def describe_role(person):
    person.role()

# Creating objects of different types
person = Person()
student = Student()
son = Son()
employee = Employee()

# Using the same function to describe roles
describe_role(person)   # Output: This is a general person
describe_role(student)  # Output: He is treated as a student at college or school
describe_role(son)      # Output: He is treated as a son at home
describe_role(employee) # Output: He is treated as an employee at the office
