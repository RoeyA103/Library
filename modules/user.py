from modules.book import Book

class User:
    id = 100
    def __init__(self, name: str, id: int = None, borrowed_books: list = None):
        self.name = name
        self.__borrowed_books = borrowed_books
        if id:
            self.id = id
            User.id = id + 1
        else:
            self.id = User.id
            User.id += 1

    def to_dict(self):
        return {
            "id": self.id,
            "name": self.name,
            "borrowed_books": [book.to_dict() for book in self.__borrowed_books]
        }

    # Optional: method to add a book to the borrowed list
    def borrow_book(self, book):
        self.__borrowed_books.append(book)

    def __str__(self):
        return f"""name:{self.name}, id:{self.id}, borrowed books:{", ".join(book.title for book in self.__borrowed_books) if self.__borrowed_books else ""}"""
    
    def add_book(self,book)-> None:
        if  isinstance(book,Book):
            self.__borrowed_books.append(book)
        else:
            raise ValueError("can add only Book object")

    def remove_book(self,book)->None:
        if isinstance(book,Book):
            self.__borrowed_books = [b for b in self.__borrowed_books if b.title != book.title]
        else:
            raise ValueError("can remove only Book object")
