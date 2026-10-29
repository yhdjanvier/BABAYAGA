#TODO ONE
from dataclasses import dataclass
import matplotlib.pyplot as plt

@dataclass
class Book:
    title:str
    author:str
    year:int
    isbn:str

    def display_details(self):
        return f"Title:{self.title}, Author:{self.author},Year:{self.year},ISBN:{self.isbn}"
book = Book(title="1984",author="George Orwell",year=1949,isbn="123-456-789") #2marks

#TODO TWO
#print(book.display_details())

                 #QUESTION 2
class Library:
    def __init__(self):
        self.books=[]
    def add_book(self,book):
        self.books.append(book)

    def remove_book_by_isbn(self,isbn):
        self.books = [book for book in self.books if book.isbn != isbn]
        return self.books
    
    def display_all_books(self):
        for book in self.books:
            print(book.display_details())
library = Library()

book1 = Book(title="1985",author="George Orwell",year=1948,isbn="003-456-789")
book2 = Book(title="1980",author="Sean Orwell",year=1948,isbn="003-496-089")
library.add_book(book1)
library.add_book(book2)

remove = library.remove_book_by_isbn("123-456-789")
if remove:
    print("book removed")
else:
    print("book not removed")
library.display_all_books()




print("========= QUESTION TWO =========")

class Person:
    def __init__(self,name,age):
        self.name = name
        self.age = age
    def display_details(self):
        return f"Name:{self.name}\nAge:{self.age}"

class Student(Person):
    def __init__(self,name,age,student_id):
        #self.name = name
        #self.age = age
        super().__init__(name,age)
        self.student_id = student_id

    def display_details(self):
        return f"Name:{self.name}\nAge:{self.age}\nStudent_Id:{self.student_id}"
    
student = Student("yhd",30,"24rp01003")
person = Person("yhd",40,)

print(student.display_details())

print(person.display_details())

book_years = [book1.year,book2.year]
book_titles = [book1.title,book2.title]

plt.figure(figsize=(10,6))
plt.bar(book_titles,book_years,color='blue')

plt.xlabel("book_titles")
plt.ylabel("book_years")
plt.title("KWEKU THE TRAVEL")
plt.tight_layout()
plt.show()