import json

class Book:
    isbn = 200
    def __init__(self, title ,author,isbn=None,__is_available=True):
        self.title = title
        self.author = author
        self.__is_available = __is_available
        if isbn:
            self.isbn = isbn
            Book.isbn = isbn + 1
        else:
            self.isbn  = Book.isbn
            Book.isbn += 1

        
    def __str__(self):
        return f" the name book is: {self.title} the author book is: {self.author} Serial number: {self.isbn}"

    def set_available(self, flag: bool) -> None:
        if isinstance(flag, bool):
            self.__is_available = flag
        else:
            raise ValueError("can add only Boolyan object")

    def is_available(self) -> bool:
        return self.__is_available

