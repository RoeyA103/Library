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

    def add_book(self,book:Book)->None:
        if isinstance(book,Book):
            self.books.append(book)
            print("The book has been successfully added")
        else:
            ValueError("did yue cen append only book of type Book")

    def add_user(self,user:User)->None:
        if isinstance(user,User):
            self.users.append(user)
            print("The user has been successfully added")
        else:
            ValueError("did yue cen append only user of type User")

    def return_book(self,user_id,book_isbn)->None:
        book = find_book(book_isbn)
        user = find_user(user_id)
        if book and user:
            book.set_available(True)
            user.remove_book(book)

    def list_available_books(self) ->list:
        list_available = [book for book in self.books if book.is_available()]
        return list_available

    