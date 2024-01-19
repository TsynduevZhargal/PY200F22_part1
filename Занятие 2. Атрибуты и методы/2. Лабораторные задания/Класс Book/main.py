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

    def __str__(self) -> str:
        return f"Книга название книги = {self.name}"

    def __repr__(self) -> str:
        return f"Book(id_=1, name='test_name_1', pages=200)"



if __name__ == '__main__':
    # инициализируем список книг
    list_books = [
        Book(id_=book_dict["id"], name=book_dict["name"], pages=book_dict["pages"]) for book_dict in BOOKS_DATABASE
    ]
    for book in list_books:
        print(book)  # проверяем метод __str__

    print(list_books)  # проверяем метод __repr__
