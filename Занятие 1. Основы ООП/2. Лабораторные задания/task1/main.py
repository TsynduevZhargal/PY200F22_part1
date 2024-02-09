from typing import Union

# TODO Написать 3 класса с документацией и аннотацией типов


class House:   # класс Дом
    def __init__(self, height: Union[int, float], material: Union[str]):
        if not isinstance(height, (int, float)):
            raise TypeError   # Не является числом
        if height <= 0:
            raise ValueError  # Не может быть отрицательной

        self.height = height     # высота (этажность)
        self.material = material   # материал
    #
    # def build_house(self, height):
    #     """
    #     Стройка дополнительных этажей
    #     param house: Количество добавляемых этажей
    #     """
    def __str__(self) -> str:
        return f"Количество этажей = {self.height}. Вид материала = {self.material}"

# TODO работоспособность экземпляров класса проверить с помощью doctest
if __name__ == "__main__":
    height = House(1, "деревянный")
    print(height)


class Car:    # класс автомобиль
    def __init__(self, speed: int, power: int):
        self.speed = speed   # скорость
        self.power = power   # мощность

    def Truck(self, power):  # мощность грузового автомобиля выше
        ...

if __name__ == "__main__":
    ...

class Suit:    # класс костюм
    def __init__(self, colour: str, size: int):
        self.colour = colour   # цвет
        self.size = size       # размер

    def men_suit(self, colour):
        ...

if __name__ == "__main__":
    ...
print()