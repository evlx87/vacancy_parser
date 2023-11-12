from abc import ABC, abstractmethod


class VacancyAPI(ABC):
    """Абстрактный класс для работы с API сайтов с вакансиями"""
    @abstractmethod
    def get_vacancies(self, keyword: str) -> None:
        """
        Получение информации о вакансиях через API
        :return: None
        """
        pass
