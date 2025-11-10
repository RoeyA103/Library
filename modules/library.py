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
    
    