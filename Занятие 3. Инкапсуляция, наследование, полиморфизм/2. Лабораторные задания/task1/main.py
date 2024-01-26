class Book:
    """ Базовый класс книги. """
    def __init__(self, name: str, author: str):
        self.name = name
        self.author = author

    def __str__(self):
        return f"Книга {self.name}. Автор {self.author}"

    def __repr__(self):
        return f"{self.__class__.__name__}(name={self.name!r}, author={self.author!r})"


class PaperBook(Book):
    def __init__(self, pages: int):
        super().__init__(name)
        self.pages = pages

    def __str__(self):
        return f"Книга {self.name}. Автор {self.author}"


class AudioBook:
    def __init__(self, name: str, author: str, duration: float):
        # self.name = name
        # self.author = author
        self.duration = duration

    def __str__(self):
        return f"Книга {self.name}. Автор {self.author}"


# наследование с базовой книги
print(PaperBook.name) # наследование с базовой книги
print(AudioBook.name)
class PaperBook(Book):
    print(PaperBook.name)

if __name__ == "__main__":
    name = (, 'rect_fig')
    rect.print_name()