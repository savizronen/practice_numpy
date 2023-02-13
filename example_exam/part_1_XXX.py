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
"""
End Area for Question 1
"""

"""
Start Area for Question 2
"""
"""
End Area for Question 2
"""

"""
Start Area for Question 3
"""
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
"""
End Area for Question 4
"""

window.mainloop()



