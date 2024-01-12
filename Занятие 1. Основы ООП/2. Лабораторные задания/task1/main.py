from typing import Union

# TODO Написать 3 класса с документацией и аннотацией типов


class House:   # Дом
    def __init__(self, low: Union[int, float], high: Union[int, float]):  # низкий или высокий
        if not isinstance(low, (int, float)):
            raise TypeError
        if low <= 0:
            raise ValueError  # Не может быть отрицательной

        if not isinstance(high, (int, float)):
            raise TypeError
        if high <= 0:
            raise ValueError   # Не может быть отрицательной

        if low > high:
            raise TypeError     # Не возможно чтобы низкий был выше высокого

        self.low = low
        self.high = high

if __name__ == "__main__":
    house1 = House(2, 10)
    print(house1.low, house1.high)
    house2 = House(8, 22)
    print(house2.low, house2.high)
    print("достроили дом № 1 на 2 этажа")
    house3 = House()
    # TODO работоспособность экземпляров класса проверить с помощью doctest
    pass
