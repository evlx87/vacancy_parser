from abc import ABC, abstractmethod
import json

from src.classes.class_vacancy import Vacancy


class FileSaver(ABC):
    """Абстрактный класс для работы с вакансиями"""

    @abstractmethod
    def add(self, vacancy: Vacancy) -> None:
        """Добавление вакансии в файл"""
        pass

    @abstractmethod
    def get(self, parameter: str) -> [dict]:
        """Получение информации о вакансии по критериям"""
        pass

    @abstractmethod
    def delete(self, vacancy: Vacancy) -> None:
        """Удаление вакансии"""
        pass

    @abstractmethod
    def clear(self):
        """Очистка файла"""
        pass


class JSONSaver(FileSaver):
    """Класс для работы с вакансиями в формате JSON"""

    def __init__(self) -> None:
        """Инициализация объекта класса"""
        self.list_vacancy = []

    def add(self, item: list[dict]) -> None:
        """
        Добавление вакансии в файл
        Args: item (list[dict]): Список словарей с информацией о вакансиях
        """
        with open('data/vacancy.json', 'w', encoding='utf-8') as f:
            json.dump(self.list_vacancy, f, indent=4, ensure_ascii=False)

    def get(self, parameter: str) -> [dict]:
        """Получение информации о вакансии по критериям"""
        pass

    def delete(self, vacancy: Vacancy) -> None:
        """Удаление вакансии"""
        pass

    def clear(self):
        """Очистка файла"""
        pass