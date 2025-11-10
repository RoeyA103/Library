class Book:
    isbn = 200
    def __init__(self, title ,author):
        self.title = title
        self.author = author
        self.isbn = Book.isbn
        self.is_available = True
        Book.isbn += 1

    def __str__(self):
        return f" the name book is: {self.title} the author book is: {self.author} Serial number: {self.isbn}"