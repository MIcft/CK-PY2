import doctest
import math


class MediaPlayer:
    """
    Класс MediaPlayer предназначен для воспроизведения видео из файла


    """

    def __init__(self, file_extension: str):
        """
         Создание и подготовка к работе объекта "MediaPlayer"
        :param file_extension: Расширение файла
        """
        if not isinstance(file_extension, str):
            raise TypeError("Расширение файла должно быть типа str")
        self.type = file_extension
        self.filename = None

    def open(self, file):
        """
        Метод открывает файл с
        Добавляет новый атрибут экземляру
        :param file: Название файла
        :return:
        """
        setattr(self, 'filename', file)

    def play(self):
        """
        Метод воспроизводит видео

        """
        print(f'Воспроизведение {self.filename}.{self.type}')


class Vector:
    """
    class Vector описывает 3 мерный вектор по координатам x, y, z
    """

    def __init__(self, x: int | float, y: int | float, z: int | float):
        """
        Создание и подготовка к работе объекта "Вектор"
        :param x: Координата x конца вектора
        :param y: Координата y конца вектора
        :param z: Координата z конца вектора
        """
        self.length = None
        if not isinstance(x | y | z, int | float):
            raise TypeError("Координаты должны быть int или float")
        self.x = x
        self.y = y
        self.z = z

    def get_length(self):
        """
        Метод для нахождения длины вектора
        :return: возращает длину вектора
        """
        self.length = abs(math.sqrt(self.x ** 2 + self.y ** 2 + self.z ** 2))
        return self.length

    def add(self, x, y, z):
        """
        Метод складывает объект с другим вектором
        :param x: координата x второго вектора
        :param y: координата y второго вектора
        :param z: координата z второго вектора

         Примеры:
        >>> v2 = Vector(1, 2, 3)
        >>> print(v2.get_length())
        3.7416573867739413
        >>> v2.add(2, 3, 4)
        >>> print(v2.get_length())
        9.1104335791443
        """
        self.x += x
        self.y += y
        self.z += z

    class Car:
        def __init__(self, power: int, volume: int | float):
            """
            Создание и подготовка к работе объекта "Машина"
            :param power: Мощность автомобиля
            :param volume: Громкость сигнала
            """
            if not isinstance(power, int):
                raise TypeError("Мощность автомобиля должна быть типа int")
            if power <= 0:
                raise ValueError("Мощность автомобиля должна быть положительным числом")
            self.power = power

            if not isinstance(volume, int | float):
                raise TypeError("Громкость сигнала должна быть int или float")
            if volume < 0:
                raise ValueError("Громкость сигнала не может быть отрицательным числом")
            self.volume = volume

        def play_buzzer(self, is_engine_rotation=False):
            """
            :param is_engine_rotation: Нажата ли педаль газа
            :return: Воспроизводит сигнал автомобиля

            """
            if not isinstance(is_engine_rotation, bool):
                raise TypeError(" engine_rotation должен быть bool")
            if is_engine_rotation:
                self.increase_engine_rotation()
            if self.volume > 5:
                print('БИБИ')
            else:
                print('биби')

        def increase_engine_rotation(self):
            """
            :return: Воспроизводит звук выхлопной системы автомобиля
            """
            print(self.power * 'vrum-vrum')


if __name__ == "__main__":
    doctest.testmod()
