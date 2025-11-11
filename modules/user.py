from modules.book import Book

class User:
    id = 100
    def __init__(self, name:str, id:int=None , __borrowed_books:list=None):
        self.name = name
        self.__borrowed_books = __borrowed_books
        if id:
            self.id = id
            User.id = id +1
        else:
            self.id = User.id
            User.id += 1

    def __str__(self):
        return f"""name:{self.name}, id:{self.id}, borrowed books:{", ".join(book.title for book in self.__borrowed_books)}"""
    
    def add_book(self,book)-> None:
        if  isinstance(book,Book):
            self.__borrowed_books.append(book)
        else:
            raise ValueError("can add only Book object")

    def remove_book(self,book)->None:
        if isinstance(book,Book):
            self.__borrowed_books.remove(book)
        else:
            raise ValueError("can add only Book object")
