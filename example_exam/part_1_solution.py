from tkinter import *
from tkinter import ttk, messagebox


class Member:
    def __init__(self, name, id):
        self.name = name
        self.id = id

    def __str__(self):
        return self.name

    def __repr__(self):
        return str(self)


class BorrowError(Exception):
    pass


class BookNotFoundError(Exception):
    pass


"""
Start Area for Question 1
"""
class Book:
    def __init__(self, title, author, publisher, isbn):
        self.title = title
        self.author = author
        self.publisher = publisher
        self.isbn = isbn
        self.borrows = []

    def __str__(self):
        return f"Title: {self.title}, Author: {self.author}, Publisher: {self.publisher}, ISBN: {self.isbn}"

    def __repr__(self):
        return str(self)

    def borrow(self, member):
        if self.is_available():
            self.borrows.append(member)
        else:
            raise BorrowError(f"The book {self.title} ({self.isbn}) already borrowed")

    def is_available(self):
        return len(self.borrows) == 0


"""
End Area for Question 1
"""

"""
Start Area for Question 2
"""
class Ebook(Book):
    def __init__(self, title, author, publisher, isbn, file_size):
        super().__init__(title, author, publisher, isbn)
        self.file_size = file_size

    def __str__(self):
        return f"{super().__str__()}, File Size: {self.file_size}"

    def borrow(self, member):
        self.borrows.append(member)


"""
End Area for Question 2
"""

"""
Start Area for Question 3
"""
class Library:
    def __init__(self, name):
        self.name = name
        self.books = []

    def add_book(self, book):
        self.books.append(book)

    def borrow_book(self, isbn, member):
        is_book_exist = False

        for book in self.books:
            if isbn == book.isbn:
                book.borrow(member)
                is_book_exist = True

        if not is_book_exist:
            raise BookNotFoundError(f"Book {isbn} not exist!")

"""
End Area for Question 3
"""


# creating instances of the classes
library = Library("Afeka public Library")

b_1 = Book("The Great Gatsby", "F. Scott Fitzgerald", "Charles Scribner's", 1)
b_2 = Ebook("The Great Gatsby", "F. Scott Fitzgerald", "Charles Scribner's", 2, 1.5)
b_3 = Book("Harry Potter and the Philosopher's Stone", "J. K. Rowling", "Bloomsbury", 3)
b_4 = Ebook("The Alchemist", "Paulo Coelho", "HarperTorch", 4, 2.15)

# adding book to the library
library.add_book(b_1)
library.add_book(b_2)
library.add_book(b_3)
library.add_book(b_4)


# List of members
member_1 = Member("John Smith", 1)
member_2 = Member("Barbara Mary", 2)
member_3 = Member("Robert James", 3)
member_4 = Member("Patricia Roberts", 4)
members = [member_1, member_2, member_3, member_4]

# helper function that get a member name and return a Member
def get_member_by_name(name):
    for member in members:
        if member.name == name:
            return member
    return None


# Define a Tkinter GUI Application
window = Tk()
window.title(library.name)

window.geometry("600x200")

lbl = Label(window, text=library.name, font=("Ariel bold", 40), fg="blue")
lbl.grid(column=0, row=0)

member_lbl = Label(window, text="Member")
member_lbl.grid(column=0, row=1)

members_combo = ttk.Combobox(window, values=members)
members_combo.grid(row=2, column=0)

isbn_lbl = Label(window, text="Book ISBN")
isbn_lbl.grid(column=1, row=1)

book_isbn_entry_txt = Entry(window, width=10)
book_isbn_entry_txt.grid(row=2, column=1)
book_isbn_entry_txt.focus()


"""
Start Area for Question 4
"""
def handel_borrow_click():
    member_name = members_combo.get()
    member = get_member_by_name(member_name)
    isbn = book_isbn_entry_txt.get()

    if not isbn.isnumeric():
        messagebox.showinfo(message=f"isbn must be a number!")
        return
    isbn = int(isbn)

    try:
        library.borrow_book(isbn, member)
        messagebox.showinfo(message=f"{member} borrow book id: {isbn}!")
    except (BookNotFoundError, BorrowError) as e:
        messagebox.showinfo(message=str(e))


btn = Button(window, text="Borrow", width=10, height=2, command=handel_borrow_click)
btn.grid(column=1, row=3)
"""
End Area for Question 4
"""

window.mainloop()



