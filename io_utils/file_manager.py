from modules.book import Book
from modules.user import User
from json import load , dump


def write_book_to_file(book:Book,path="database\\books.json")->None:
    """
    Saves the object in json format
(parameter extraction is done in the function itself)
(default path database\\books.json)
"""

    with open(path, "a") as file:
        dump(book.__dict__, file, indent=4)


def read_books_from_file(path="database\\books.json") ->list[Book] | None:
    try:
        with open(path, "r") as file:
            books = load(file)
        return books
    except:
        return None


def write_user_to_file(user:User,path="database\\users.json")->None:
    """
    Saves the object in json format
(parameter extraction is done in the function itself)
(default path database\\users.json)
"""

    with open(path, "a") as file:
        dump(user.__dict__, file, indent=4)

def read_users_from_file(path = "database\\users.json") ->list[User] | None:
    try:
        with open(path, "r") as file:
            users = load(file)
        return users
    except:
        return None


