
from dataclasses import dataclass
import matplotlib.pyplot as plt


# ==================================================
# PART 1: BOOK CLASS
# ==================================================

@dataclass
class Book:
    title: str
    author: str
    year: int
    isbn: str

    def display_details(self):
        return (
            f"Title: {self.title}, Author: {self.author}, "
            f"Year: {self.year}, ISBN: {self.isbn}"
        )


# TODO 1 and TODO 2: Create and display one book
book = Book(
    title="1984",
    author="George Orwell",
    year=1949,
    isbn="123-456-789"
)

print("ONE BOOK")
print(book.display_details())


# ==================================================
# PART 2: LIBRARY MANAGEMENT
# ==================================================

class Library:
    def __init__(self):
        self.books = []

    def add_book(self, book):
        self.books.append(book)

    def remove_book_by_isbn(self, isbn):
        original_count = len(self.books)

        self.books = [
            book for book in self.books
            if book.isbn != isbn
        ]

        return len(self.books) < original_count

    def display_all_books(self):
        if not self.books:
            print("The library has no books.")
            return

        for book in self.books:
            print(book.display_details())


library = Library()

# TODO 3: Create two book instances
book1 = Book(
    title="1984",
    author="George Orwell",
    year=1949,
    isbn="123-456-789"
)

book2 = Book(
    title="Animal Farm",
    author="George Orwell",
    year=1945,
    isbn="987-654-321"
)

# TODO 4: Add the books to the library
library.add_book(book1)
library.add_book(book2)

# TODO 5: Display all books
print("\nALL BOOKS IN THE LIBRARY")
library.display_all_books()

# TODO 6: Remove a book and display again
print("\nREMOVING BOOK")
removed = library.remove_book_by_isbn("123-456-789")

if removed:
    print("Book removed successfully.")
else:
    print("Book not found.")

print("\nREMAINING BOOKS")
library.display_all_books()


# ==================================================
# PART 3: INHERITANCE AND POLYMORPHISM
# ==================================================

class Person:
    def __init__(self, name, age):
        self.name = name
        self.age = age

    def display_details(self):
        return f"Name: {self.name}, Age: {self.age}"


class Student(Person):
    def __init__(self, name, age, student_id):
        super().__init__(name, age)
        self.student_id = student_id

    # Method overriding
    def display_details(self):
        return (
            f"Name: {self.name}, Age: {self.age}, "
            f"Student ID: {self.student_id}"
        )


# TODO 7: Create Person and Student objects
person1 = Person(name="David", age=30)
student1 = Student(
    name="Bob",
    age=20,
    student_id="S12345"
)

# TODO 8 and TODO 9: Display details
print("\nPERSON DETAILS")
print(person1.display_details())

print("\nSTUDENT DETAILS")
print(student1.display_details())


# Demonstrate polymorphism
print("\nPOLYMORPHISM")
people = [person1, student1]

for person in people:
    print(person.display_details())


# ==================================================
# PART 4: PLOT BOOK PUBLICATION YEARS
# ==================================================

# TODO 10: Prepare the data
book_years = [book1.year, book2.year]
book_titles = [book1.title, book2.title]

plt.figure(figsize=(10, 6))
plt.bar(book_titles, book_years, color="blue")
plt.xlabel("Book Title")
plt.ylabel("Publication Year")
plt.title("Books and Their Publication Years")
plt.show()
