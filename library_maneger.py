from modules.book import Book
from modules.user import User
from modules.library import Library
from json import dumps , loads ,load , dump
from types import SimpleNamespace
import os

b1 = Book("bla","blu")
b2 = Book("ddada","dedede")
b3 = Book("lolol","lalal")

print(os.path('test.txt'))

# books = [b1.__dict__, b2.__dict__, b3.__dict__]

# with open("test.txt", "w") as file:
#     dump(books, file,indent=4)

# with open("test.txt", "r") as file:
#     books1 = load(file)

# self.books =  [Book(**book) for book in books1]

# print(books1)
    
    
# [print(book.isbn) for book in books1]
# print(Book.isbn)

