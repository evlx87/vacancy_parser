import uuid

from src.classes.class_api import HeadHunterAPI
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
