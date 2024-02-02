from typing import Union


class Glass:
    def __init__(self, capacity_volume: Union[int, float], occupied_volume: Union[int, float]):
        if not isinstance(capacity_volume, (int, float)):
            raise TypeError("Неправильный тип данных")
        if capacity_volume <= 0:
            raise ValueError("Невозможна отрицательная величина")

        if not isinstance(occupied_volume, (int, float)):
            raise TypeError("Неправильный тип данных")
        if occupied_volume <= 0:
            raise ValueError("Невозможна отрицательная величина")

        if occupied_volume > capacity_volume:
            raise TypeError("Вместимость меньше желаемого заполнения")
        self.capacity_volume = capacity_volume  # TODO инициализировать объект "Стакан"
        self.occupied_volume = occupied_volume


if __name__ == "__main__":
    glass1 = Glass(200, 100)  # TODO инициализировать два объекта типа Glass
    print(glass1)
    glass2 = Glass(500, 50)   # необходимо обезопасить ввод неправильных данных и проверить

    # TODO попробовать инициализировать не корректные объекты
