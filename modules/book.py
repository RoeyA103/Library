class Book:
    isbn = 200
    def __init__(self, title ,author):
        self.title = title
        self.author = author
        self.isbn = Book.isbn
        self.__is_available = True
        Book.isbn += 1

    def __str__(self):
        return f" the name book is: {self.title} the author book is: {self.author} Serial number: {self.isbn}"

    def set_available(self,flag:bool):
        if isinstance(flag,bool):
            self.__is_available = flag
        else:
            raise ValueError("can add only Boolyan object")

    def is_available(self):
        return self.__is_available

