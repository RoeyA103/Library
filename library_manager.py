from modules.book import Book
from modules.user import User
from modules.library import Library
from io_utils.file_manager import *
from io_utils.ios import *
from json import dumps , loads ,load , dump


class Manager:
    def __init__(self):
        self.library = Library()
        self.library.books = Manager.load_books() 
        self.library.users = Manager.load_users()

    @classmethod
    def load_books(cls):
        if books := read_books_from_file():
            return [Book(**data) for data in books]
        return []

    @classmethod
    def load_users(cls):
        if users := read_users_from_file():
            return [User(**data) for data in users]
        return []

            
    def create_user(self)-> User:
        user_name = input("enter user name:\n")
        user = User(user_name)
        write_user_to_file(user)

        return user
    
    def create_book(self)-> Book:
        book_title = input("enter book title:\n")
        book_author = input("enter book  author")
        book = Book(book_title,book_author)
        write_book_to_file(book)
        return book
    def delete_user(self,user_id):
        self.library.delelt_user(user_id)
        delete_user_from_file(user_id)

    def delete_book(self,book_isbn):
        self.library.delete_book(book_isbn)
        delete_book_from_file(book_isbn)

    def sign_user(self,user:User):
        self.library.add_user(user)
        write_user_to_file(user)

    def sign_book(self,book:Book):
        self.library.add_book(book)
        write_book_to_file(book)


