"""
type of inheritance :
    if we inherit the feature and method form multiple parent class to any one child class then  it is called multiple inheritance
    
    Example :
"""

class Father :
    def land(self):
        print("land")
class Mother:
    def jewellery(self):
        print("Jewelleries")
class Daughter(Father, Mother):
    pass
daughter = Daughter()
daughter.land()
daughter.jewellery()

print("\nNew Class : \n")

class Person :
    def display(self):
        print("hello world")
class Student(Person):
    pass
class Teacher(Person):
    pass
std = Student()

std.display()

Polymorphism