import json
import uuid

from src.classes.class_api import HeadHunterAPI
from src.classes.class_vacancy import Vacancy
from src.file_saver import JSONSaver


def get_hh_vacancies(vacancy: list[dict]) -> list[dict]:
    """Форматирование объектов hh.ru"""
    vacancy_object = [{
        'id': str(uuid.uuid4()),
        'title': item['name'],
        'link': item['alternate_url'],
        'salary': item['salary']['from'] if item.get('salary') else '0',
        'requirements': item['snippet']['requirement']
    } for item in vacancy]
    return vacancy_object


def unique_value_counter(data):
    unique_ids = set()
    for d in data:
        unique_ids.add(d['id'])
    return unique_ids


def parser_run():
    keyword = input('Введите поисковой запрос: ')
    hh_api = HeadHunterAPI()

    vacancies_hh = get_hh_vacancies(hh_api.get_vacancies(keyword))

    uvc = unique_value_counter(vacancies_hh)

    json_saver = JSONSaver()
    json_saver.add(vacancies_hh)

    print(f"Поиск вакансий по запросу '{keyword}' завершен.\n"
          f"Добавлено {len(uvc)} вакансий в файл vacancy.json")


def sorted_by_salary(vacancy: list[Vacancy]) -> list[Vacancy]:
    """Сортировка по зарплате"""
    return sorted(vacancy, reverse=True)


def vacancy_output(res: list[Vacancy]) -> None:
    """Вывод вакансий в удобном для пользователя виде"""
    for i, v in enumerate(res):
        print(f"{i + 1}. "
              f"Название: {v.title}\n"
              f"Зарплата от {v.salary}\n"
              f"Ссылка: {v.link}\n"
              f"+++++++++++")


def output_by_quantity(vacancy: list[Vacancy], quantity: int) -> list[Vacancy]:
    """Вывод вакансий по заданному количеству"""
    return vacancy[:quantity]


def get_vacancies_from_json(vacancies):
    quantity = int(input("Введите нужное количество вакансий для вывода: "))
    test = output_by_quantity(vacancies, quantity)
    return vacancy_output(test)

