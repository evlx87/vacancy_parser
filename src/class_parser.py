import requests
from src.class_api import VacancyAPI


class HeadHunterAPI(VacancyAPI):
    """Класс для работы с API hh.ru"""
    def __init__(self, url='https://api.hh.ru/vacancies') -> None:
        self.__base_url = url

    @property
    def url(self) -> str:
        return self.__base_url

    def get_vacancies(self, keyword: str) -> None:
        """Получение информации о вакансиях через API"""
        url = f'{self.__base_url}?text={keyword}'
        response = requests.get(url)

        if response.status_code == 200:
            vacancies = response.json()['items']
            return vacancies
        else:
            print(f'Ошибка при выполнении запроса: {response.status_code}')
