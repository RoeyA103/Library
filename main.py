from modules.book import Book
from modules.user import User
from modules.library import Library
from io_utils.file_manager import *
from io_utils.ios import *
import library_manager


def main():
    manager = library_manager.Manager()

    while True:
        print_menu()

        user_choice = input()

        match user_choice:
            case '1':
                user = manager.create_user()
                manager.sign_user(user)
            case '2':
                book = manager.create_book()
                manager.sign_book(book)
            case '3':
                book_id = get_id("enter book id:\n")
                if book := manager.library.find_book(book_id):
                    print(book)
            case '4':
                manager.library.search_book_by_title(input("enter title:\n"))
            case '5':
                manager.library.search_book_by_author(input("enter author name:\n"))
            case '6':
                user_id = get_id("enter user id:\n")
                if user := manager.library.find_user(user_id):
                    print(user)
            case '7':
                print(manager.library.list_available_books())
            case '8':
                user_id = get_id("enter user id:\n")
                book_id = get_id("enter book id:\n")
                manager.library.borrow_book(user_id,book_id)
            case '9':
                user_id = get_id("enter uder id")
                book_id = get_id("enter book id")
                manager.library.return_book(user_id,book_id)
            case '0':
                break
            case _:
                print("invalid input")
                continue

if __name__ == "__main__":
    main()