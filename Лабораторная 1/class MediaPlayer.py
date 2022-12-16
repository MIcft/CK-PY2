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
        '''
        Метод воспроизводит видео
        '''
        print(f'Воспроизведение {self.filename}.{self.type}')



