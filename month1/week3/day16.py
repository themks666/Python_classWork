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

"""
Polymorphism :
    poly = many
    morphism = forms
    It is a feature of OOP in which a 'Method' have different forms
    
    --> it can be achieved in two ways :
        1) method overriding
        2) Method overloading
        
Method Overriding :
    A process in which the method of parent class is overridie by the child class to the same method name 
"""

class Animal:
    def sound(self):
        print("Animal Sound")
class Dog(Animal):
    def sound(self):
        print("Bark")
class Cat(Animal):
    def sound(self):
        print("Meow")
        
cat = Cat()

cat.sound()

class Calculation:
    def area(self):
        print("Area")
class reactangle(Calculation):
    def __init__(self, lenght, breadth):
        self.length = lenght;
        self.breadth = breadth
    def area(self):
        print("Area of reactangle : ", self.length*self.breadth)
class Circle(Calculation):
    def __init__(self, radius):
        self.radius = radius;
    def area(self):
        print(f"Area of circle : {3.14 *self.radius**2}")
        
circle = Circle(3)
circle.area()
ract = reactangle(2,4 )
ract.area()

"""
method overloading :
    it is a process of creating same name menthod in a classs with different length of parameters
    --> Default argument concept is used for method overloading
    --> In reality method overloading is not acheived in python like c++, java
"""