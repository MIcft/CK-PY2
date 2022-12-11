import doctest
import math
class Vector:
    '''
    class Vector описывает 3 мерный вектор по координатам x, y, z
    '''
    def __init__(self, x: int | float, y: int | float, z: int | float):
        """
        Создание и подготовка к работе объекта "Вектор"
        :param x: Координата x конца вектора
        :param y: Координата y конца вектора
        :param z: Координата z конца вектора
        """
        if not isinstance(x | y | z, int | float):
            raise TypeError("Координаты должны быть int или float")
        self.x = x
        self.y = y
        self.z = z

    def getLenght(self):
        '''
        Метод для нахождения длины вектора
        :return: возращает длину вектора
        '''
        getLength = abs(math.sqrt(self.x ** 2 + self.y ** 2 + self.z ** 2))
        return getLength

    def add(self, x, y, z):
        '''
        Метод складывает объект с другим вектором
        :param x: координата x второго вектора
        :param y: координата y второго вектора
        :param z: координата z второго вектора

         Примеры:
        >>> v2 = Vector(1, 2, 3)
        >>> print(v2.getLenght())
        3.7416573867739413
        >>> v2.add(2, 3, 4)
        >>> print(v2.getLenght())
        9.1104335791443
        '''
        self.x += x
        self.y += y
        self.z += z

if __name__ == "__main__":
    doctest.testmod()
