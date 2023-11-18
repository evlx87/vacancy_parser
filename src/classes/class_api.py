from abc import ABC, abstractmethod
from http import HTTPStatus
from typing import Any

import requests

from src.config import SJ_API_KEY


class VacancyAPI(ABC):
    """Абстрактный класс для работы с API сайтов с вакансиями"""

    @abstractmethod
    def get_vacancies(self, keyword: str) -> None:
        """
        Получение информации о вакансиях через API
        :return: None
        """
        pass


class HeadHunterAPI(VacancyAPI):
    """Класс для работы с API hh.ru"""

    def __init__(self, url='https://api.hh.ru/vacancies') -> None:
        """
        Инициализирует объект класса HeadHunterAPI.
        Args: url (str, optional): Базовый URL для API. По умолчанию 'https://api.hh.ru/vacancies'.
        """
        self.__base_url = url

    @property
    def url(self) -> str:
        """
        Возвращает базовый URL для API.
        Returns: str: Базовый URL для API.
        """
        return self.__base_url

    def get_vacancies(self, keyword: str) -> str | Any:
        """
        Получает информацию о вакансиях через API.
        Args: keyword (str): Ключевое слово для поиска вакансий.
        Returns:
            str | Any: Список вакансий, если запрос выполнен успешно, иначе сообщение об ошибке.
        """
        url = f'{self.__base_url}?text={keyword}'
        response = requests.get(url)

        if response.status_code == 200:
            vacancies = response.json()['items']
            return vacancies

        return f'Ошибка при выполнении запроса: {response.status_code}'


class SuperJobAPI(VacancyAPI):

    def __init__(self):
        self.__base_url = "https://api.superjob.ru/2.0/vacancies/"
        self.headers = {"X-Api-App-Id": SJ_API_KEY}

    def get_vacancies(self, keyword):
        """Метод для получения вакансий в формате JSON"""
        params = {
            "keyword": keyword,
            "page": "1"
        }
        response = requests.get(self.__base_url,
                                params=params,
                                headers=self.headers)

        if not response.status_code == HTTPStatus.OK:
            return f'Ошибка при выполнении запроса: {response.status_code}'

        return response.json()['objects']
