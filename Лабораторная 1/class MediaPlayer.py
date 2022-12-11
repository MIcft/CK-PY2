class MediaPlayer:
    """
    Класс MediaPlayer предназначен для воспроизведения видео из файла
    """
    def __init__(self, type: str):
        """
         Создание и подготовка к работе объекта "MediaPlayer"
        :param type: Расширение файла
        """
        if not isinstance(type, str):
            raise TypeError("Расширение файла должно быть типа str")
        self.type = type
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
        '''
        Метод воспроизводит видео
        '''
        print(f'Воспроизведение {self.filename}.{self.type}')
if __name__ == '__main__':
    media1 = MediaPlayer('mp3')
    media2 = MediaPlayer('avi')
    media1.open('filemedia1')
    media2.open('filemedia2')
    media1.play()
    media2.play()