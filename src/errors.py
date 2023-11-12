class GetError(Exception):
    """Класс исключения получения данных"""
    def __init__(self, text='Параметр отсутствует'):
        super().__init__(text)


class DeleteError(Exception):
    """Класс исключения удаления"""
    def __init__(self, text='В файле отсутствует требуемая вакансия'):
        super().__init__(text)
