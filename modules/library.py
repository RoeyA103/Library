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

    def find_user(self, user_id: int) -> User | None:
        for user in self.users:
            if user.id == user_id:
                return user
        return None
    
    def find_book(self,book_id:int)-> Book | None:
        for book in self.books:
            if book.id == book_id:
                return book
        return None

    def borrow_book(self, user_id: int, book_id: int) -> None:
        user = self.find_user(user_id)
        book = self.find_book(book_id)
        if user and book:
            book.set_available(False)
            user.add_book(book)
        else:
            print("book or user not found")

    def search_book(self, book_author: str, book_title: str) -> bool:
        for book in self.books:
            if book.auther == book_author or book.title == book_title:
                return True
        return False

    def add_book(self, book: Book) -> None:
        if isinstance(book, Book):
            self.books.append(book)
            print("The book has been successfully added")
        else:
            ValueError("did yue cen append only book of type Book")

    def add_user(self, user: User) -> None:
        if isinstance(user, User):
            self.users.append(user)
            print("The user has been successfully added")
        else:
            ValueError("did yue cen append only user of type User")

    def return_book(self, user_id, book_isbn) -> None:
        book = self.find_book(book_isbn)
        user = self.find_user(user_id)
        if book and user:
            book.set_available(True)
            user.remove_book(book)
        else:
            print("book or user not found")

    def list_available_books(self) -> str:
        list_available = [book.title for book in self.books if book.is_available()]
        return ", ".join(list_available)

