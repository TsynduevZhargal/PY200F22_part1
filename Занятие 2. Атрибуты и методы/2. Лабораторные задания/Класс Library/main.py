
from node import Node

BOOKS_DATABASE = [
    {
        "id": 1,
        "name": "test_name_1",
        "pages": 200,
    },
    {
        "id": 2,
        "name": "test_name_2",
        "pages": 400,
    }
]


# TODO написать класс Book
class Book:
    def __init__(self, id, name, pages):
        self.id = id         # идентификатор книги
        self.name = name     # Название книги
        self.pages = pages   # количество страниц в книге

# TODO написать класс Library

class Library:
    def __init__(self, books):
        self.books = books   # Список книг

    def append(self, value:   ):  # записать метод
        append_node = Node(value)
        if self. is None:
            self.get_next_book_id = append_node
        else:
            last_node = self.get_next_book_id(self.books - 1)
            self.get_next_book_id(last_node, append_node)
        self.books = + 1




if __name__ == '__main__':
    empty_library = Library()  # инициализируем пустую библиотеку
    print(empty_library.get_next_book_id())  # проверяем следующий id для пустой библиотеки

    list_books = [
        Book(id_=book_dict["id"], name=book_dict["name"], pages=book_dict["pages"]) for book_dict in BOOKS_DATABASE
    ]
    library_with_books = Library(books=list_books)  # инициализируем библиотеку с книгами
    print(library_with_books.get_next_book_id())  # проверяем следующий id для непустой библиотеки

    print(library_with_books.get_index_by_book_id(1))  # проверяем индекс книги с id = 1
