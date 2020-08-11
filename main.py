# Object Oriented Programming

# Class - Template
# Object - Something Which Is Made Using The Template - Technically it is called instance of the class

# DRY - Do Not Repeat Yourself

# class Student:
#     pass
#
# harry = Student()
# larry = Student()
#
# # # These are called instance variables
# # harry.name = "Harry"
# # harry.std = 12
# # harry.section = "a"
#
# print(harry.section)

class Employee():
    numberofleaves = 8

    def __init__(self, name, salary, role, languages):
        self.name = name
        self.salary = salary
        self.role = role
        self.languages = languages

    def printdetails(self):
        return f"Name: {self.name}, Salary: {self.salary}, Role: {self.role}"

    @classmethod
    def changeleaves(cls, newleaves):
        cls.numberofleaves = newleaves

    # Alternative Constructor
    @classmethod
    def fromdash(cls, string):
        return cls(*string.split("-"))

    @staticmethod
    def printgood(string):
        print("This is good: " + string)


# It containes all the things that Employee class have plus some additional stuff
class Programmer(Employee):
    # It needs all the characteristics of an Employee Class + More

    def __init__(self, name, salary, role, languages):
        self.name = name
        self.salary = salary
        self.role = role
        self.languages = languages

    def printprog(self):
        return f"Programmer's Name is: {self.name}, Salary: {self.salary}, Role: {self.role}, Languages: {self.languages}"

# harry = Employee("Harry", 10000, "Instructor")
# rohan = Employee("Rohan", 100, "Student")
# karan = Programmer.fromdash("Karan-480-Student")

# harry.name = "Harry"
# harry.role = "Instructor"
# harry.salary = 30000
#
# rohan.name = "Rohan"
# rohan.role = "Student"
# rohan.salary = 1000

# Employee.numberofleaves = 10 # It will affect overall level - class variable
# rohan.numberofleaves = 15 # It will affect only on rohan level - instance variable
# print(harry.numberofleaves, rohan.numberofleaves)
# print(rohan.__dict__)
# print(rohan.__class__)

shubham = Programmer("Shubham", 555, "Programmer", ["Python", "Java", "C"])
karan = Programmer("Karan", 777, "Programmer", ["C++", "PHP", "JS"])

karan.printgood("karan")
print(karan.printprog())