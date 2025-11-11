from modules.book import Book
from modules.user import User
from modules.library import Library
from io import file_manager
from json import dumps , loads ,load , dump


class Manager:
    def __init__(self):
        self.library = Library()
        self.library.books = Manager.load_books() 
        self.library.users = Manager.load_users()

    @classmethod
    def load_books(cls):
        if (books := file_manager.read_books_from_file()):
            return [Book(**data) for data in books]
        return [] 

    @classmethod
    def load_users(cls):
        if (users := file_manager.read_users_from_file()):
            return [User(**data) for data in users]
        return []

            
    def creat_user(self)-> User:
        user_name = input("enter user name:\n")
        user = User(user_name)
        return user
    
    def creat_book(self)-> Book:
        book_title = input("enter book title:\n")
        book_author = input("enter book  author")
        return Book(book_author,book_title)
    
    def sign_user(self,user:User):
        self.library.add_user(user)
        file_manager.write_user_to_file(user)

    def sign_book(self,book:Book):
        self.library.add_book(book)
        file_manager.write_book_to_file(book)


