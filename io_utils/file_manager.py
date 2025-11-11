from modules.book import Book
from modules.user import User
from json import load , dump


def write_book_to_file(book:Book,path="database\\books.json")->None:
    """
    Saves the object in json format
(parameter extraction is done in the function itself)
(default path database\\books.json)
"""
    try:
        with open(path, "r") as file:
            data = load(file)
    except (FileNotFoundError, ValueError):
        data = []

    data.append(book.to_dict())

    with open(path, "w") as file:
        dump(data, file, indent=4)


def read_books_from_file(path="database\\books.json") ->list[Book] | None:
    try:
        with open(path, "r") as file:
            books = load(file)
        return books
    except:
        return None

def delete_user_from_file(user_id,path="database\\users.json")->None:
    with open(path, "r") as file:
        data = load(file)
    if data:
        for user in data:
            if user['id'] == user_id:
                data.remove(user)
                break
        with open(path, "w") as file:
            dump(data, file, indent=4)



def delete_book_from_file(book_isbn,path="database\\books.json"):
    with open(path, "r") as file:
        data = load(file)
    if data:
        for book in data:
            if book['isbn'] == book_isbn:
                data.remove(book)
                break
        with open(path, "w") as file:
            dump(data, file, indent=4)
            
def write_user_to_file(user:User,path="database\\users.json")->None:
    """
    Saves the object in json format
(parameter extraction is done in the function itself)
(default path database\\users.json)
"""

    try:
        with open(path, "r") as file:
            data = load(file)
    except (FileNotFoundError, ValueError):
        data = []

    data.append(user.to_dict())

    with open(path, "w") as file:
        dump(data, file, indent=4)

def read_users_from_file(path = "database\\users.json") ->list[User] | None:
    try:
        with open(path, "r") as file:
            users = load(file)
        return users
    except:
        return None

def update_user_data(users:list,path="database\\users.json"):
    data = [user.to_dict() for user in users]
    with open(path, "w") as file:
        dump(data, file, indent=4)

def update_book_data(books:list,path="database\\books.json"):
    data = [book.to_dict() for book in books]
    with open(path, "w") as file:
        dump(data, file, indent=4)
