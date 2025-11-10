class User:
    id = 100
    def __init__(self,name:str,id:int):
        self.name = name
        self.id = User.id
        User.id += 1
        self.borrowed_books = []

    def __str__(self):
        return f"""name:{self.name}, id:{self.id},
        borrowed books:{", ".join(book.title for book in self.borrowed_books)}"""
    
    