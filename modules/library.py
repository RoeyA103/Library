from modules.book import Book
from modules.user import User
class Library:
    def __init__(self):
        self.books = []
        self.users = []

    def __str__(self):
        books = ", ".join(book.title for book in self.books)
        users = ", ".join(user.name for user in self.users)
        return f"books: {books}\nusers: {users}"
    
    def find_user(self, user_id: int) -> User:
        for user in self.users:
            if user.id == user_id:
                return user
        return None
    
    def find_book(self,book_id:int)-> Book:
        for book in self.bookss:
            if book.id == book_id:
                return book
        return None
    
    def borrow_book(self,user_id:int,book_id:int)-> None:
        user = self.find_user(user_id)
        book = self.find_book(book_id)
        book.set_available(False)
        user.add_book(book)

    def search_book(self,book_outhor:str,book_title:str)-> bool:
        for book in self.books:
            if book.outher == book_outhor or book.title == book_title:
                return True
        return False
   