class Car:
    def __init__(self, power:int , volume:int | float):
        '''
        Создание и подготовка к работе объекта "Машина"
        :param power: Мощность автомобиля
        :param volume: Громкость сигнала
        '''
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

    def bibi(self):
        """
        :return: Воспроизводит сигнал автомобиля
        """
        if self.volume > 5:
            print('БИБИ')
        else:
            print('биби')

    def vrumvrum(self):
        '''
        :return: Воспроизводит звук выхлопной системы автомобиля
        '''
        print(self.power * 'vrum-vrum')

