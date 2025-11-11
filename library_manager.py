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
        users_data = read_users_from_file()
        if not users_data:
            return []

        users = []
        for data in users_data:
            borrowed_books = [Book(**book) for book in data.get('borrowed_books', [])]
            data['borrowed_books'] = borrowed_books
            users.append(User(**data))

        return users


            
    def create_user(self)-> User:
        user_name = input("enter user name:\n")
        user = User(user_name)
        print(user)

        return user
    
    def create_book(self)-> Book:
        book_title = input("enter book title:\n")
        book_author = input("enter book  author:\n")
        book = Book(book_title,book_author)
        print(book)

        return book
    
    def sign_user(self,user:User):
        self.library.add_user(user)
        write_user_to_file(user)

    def sign_book(self,book:Book):
        self.library.add_book(book)
        write_book_to_file(book)


    def borrow_book(self,user_id ,book_id):
        self.library.borrow_book(user_id,book_id)
        update_book_data(self.library.books)
        update_user_data(self.library.users)
    

    def return_book(self,user_id,book_id):
        self.library.return_book(user_id,book_id)
        update_book_data(self.library.books)
        update_user_data(self.library.users)