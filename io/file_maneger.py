from modules.book import Book
from modules.user import User
from json import load , dump


def write_book_to_file(book:Book)->None:
    with open("test.json", "a") as file:
        dump(book.__dict__, file, indent=4)


def read_books_from_file() ->list[Book]:
    with open("test.json", "r") as file:
        books = load(file)
    return books


def write_user_to_file(user:User)->None:
    with open("test.json", "a") as file:
        dump(user.__dict__, file, indent=4)

def read_users_from_file() ->list[User]:
    with open("test.json", "r") as file:
        users = load(file)
    return users


