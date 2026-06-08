class Atm:
    def __init__(self, name, balance):
        self.name = name;
        self.balance = balance;
    def update_balance(self):
        self.balance += 5000
    def display_balance(self):
        print(f"name : {self.name}\nbalance : {self.balance}")
        
user1 = Atm("manish", 10000)
user1.display_balance()
user1.update_balance()
user1.display_balance() 

"""
A process of inheriting the feature of parent class to the child class is known as inheritance

inheritance removes the code duolicacy

syntax :
    class Person:
        #statement
    class Student(Person):
        #statement

In the above syntac, we can use the properties and method of parent class (Person) into the child class (Student) as we are inheriting it
    
"""


#TODO: program to iumplement "Inheritance"
class Person:
    def __init__(self, name, age):
        self.name = name
        self.age = age
    def display(self):
        print(f"name : {self.name}\nage : {self.age}")
        

class Student(Person):
    def __init__(self, name, age, gender):
        super().__init__(name, age)
        self.gender = gender
    def display_student(self):
        print(f"name : {self.name}\nage : {self.age}\ngender : {self.gender}")
class Teacher(Person):
    pass

std = Student("Manish", 23, "male")
teacher = Teacher('Diya', 29)
std.display_student()
teacher.display()

"""
 In the above class we are creating a person class and inheriting it to two different classes that is Student and Teacher 
"""


"""
Types of Inheritance:
    simple Inheritance:
        when we inherit feature of one class to another only one class then it is called simple inheritance
    Multi Level Inheritance:
        Deriving feature from one parent class which is driving the feature from another parent class
"""