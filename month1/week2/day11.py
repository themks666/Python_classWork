class Car:
    def __init__(self, name,price):
        self.name = name 
        self.price = price
    def display(self):
        print(f"name : {self.name} \n price : {self.price}")
c1= Car("mazda",60000)
c1.display()


class book:
    def __init__(self, name, releaseDate):
        self.bookName = name
        self.releaseDate = releaseDate

book1 = book("rich dad poor dad", 2007)
book2 = book("harry potter", 2005)
book3 = book("matilda", 1998)

'''

if(book1.releaseDate> book2.releaseDate) and (book1.releaseDate> book3.releaseDate):
    print(f"latest book : {book1.bookName}")

elif(book2.releaseDate> book1.releaseDate) and (book2.releaseDate> book3.releaseDate):
    print(f"latest book : {book2.bookName}")
else:
    print(f"latest book : {book3.bookName}")
'''
    
    
books =[
    book("a", 2014)，
    book("b", 2015)，
    book("c", 2016)，
    book("d", 2017)，
    book("e", 2018)
]