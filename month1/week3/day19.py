"""
instance varuable :
    variables associated with any specific objects aew instance variable.
    those values created for one object are not available for other objects.
"""
#Example :

class student:
    CollegeName = "Orchid college of technology and Management"
    def __init__(self, name, age):
        self.name = name
        self.age = age
    def display(self):
        print(f"Name : {self.name}\nage : {self.age}")


sdt1 = student("Manish", 20)
sdt1 = student("resham", 24)
print(sdt1.CollegeName)
sdt1.display()


class temperature :
    def convertCelciusTOFarenhit(c):
        return 1.8*c+32
print(temperature.convertCelciusTOFarenhit(34))