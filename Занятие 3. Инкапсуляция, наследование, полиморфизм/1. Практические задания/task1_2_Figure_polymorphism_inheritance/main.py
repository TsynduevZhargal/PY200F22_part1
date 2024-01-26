import math


class Figure:
    """ Базовый класс. """

    def area(self):
        print(f"Вызван метод класса {self.__class__.__name__}")
        return None


class Rectangle(Figure):
    """ Производный класс. Прямоугольник. """
    self __init__ (self a, b)
    return   # TODO определить конструктор и перегрузить метод area

    def area(self):
        super().area()
        return self.a = self/b

class Circle(Figure):
    """ Производный класс. Круг. """
    def __init__(self):
    def area(self):
        return math.pi * (self.a**2)  # TODO определить конструктор и перегрузить метод area


if __name__ == "__main__":
    fig = Figure()
    fig.area()

    rect = Rectangle(5, 10)
    (rect.area()

    circle = Circle(5)
    (circle.area()