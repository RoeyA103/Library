from modules.book import Book
from modules.user import User
from modules.library import Library
from io.file_maneger import *
import library_maneger

def print_menu():
    print(f"""
Welcome to the library management program
----------------------------------------------
To create a new user, press 1
To create a new book, press 2
To search for a book by id, press 3
To search for a book by name or author, press 4
To search for a user by id, press 5
To view a list of available books, press 6
To borrow a book, press 7
To return a book, press 8
---------------------------------------------
          """)

def main():
    while True:
        maneger = library_maneger.Maneger()
        