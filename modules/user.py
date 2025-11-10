from modules.book import Book
class User:
    id = 100
    def __init__(self,name:str,id:int):
        self.name = name
        self.id = User.id
        User.id += 1
        self.__borrowed_books = []

    def __str__(self):
        return f"""name:{self.name}, id:{self.id},
        borrowed books:{", ".join(book.title for book in self.__borrowed_books)}"""
    
    def add_book(self,book)-> None:
        if  isinstance(Book,book):
            self.__borrowed_books.append(book)
        else:
            raise ValueError("can add only Book object")