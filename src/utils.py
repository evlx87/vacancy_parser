import uuid

from src.classes.class_api import HeadHunterAPI, SuperJobAPI
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


def get_sj_vacancies(vacancy: list[dict]) -> list[dict]:
    """Форматирование объектов SuperJob"""
    vacancy_object = [{
        'id': str(uuid.uuid4()),
        'title': item['profession'],
        'link': item['link'],
        'salary': item['payment_from'],
        'requirements': item['candidat']
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
    sj_api = SuperJobAPI()

    vacancies_hh = get_hh_vacancies(hh_api.get_vacancies(keyword))
    vacancies_sj = get_sj_vacancies(sj_api.get_vacancies(keyword))

    uvc = unique_value_counter(vacancies_hh + vacancies_sj)

    json_saver = JSONSaver()
    json_saver.add(vacancies_hh)
    json_saver.add(vacancies_sj)

    print(f"Поиск вакансий по запросу '{keyword}' завершен.\n"
          f"Добавлено {len(uvc)} вакансий в файл vacancy.json")


def sorted_by_salary(vacancy: list[Vacancy]) -> list[Vacancy]:
    """Сортировка по зарплате"""
    return sorted(vacancy, reverse=True)


def vacancy_output(res: list[Vacancy]) -> None:
    """Вывод вакансий в удобном для пользователя виде"""
    for i, v in enumerate(res):
        print(f"{i + 1}. "
              f"\t{v.title}\n"
              f"\tЗарплата от {v.salary}\n"
              f"\tТребования: {v.requirements}\n"
              f"\tСсылка: {v.link}\n"
              f"+++++++++++")


def output_by_quantity(vacancy: list[Vacancy], quantity: int) -> list[Vacancy]:
    """Вывод вакансий по заданному количеству"""
    return vacancy[:quantity]


def get_vacancies_from_json(vacancies):
    quantity = int(input("Введите нужное количество вакансий для вывода: "))
    test = output_by_quantity(vacancies, quantity)
    sorted_by_salary(test)
    return vacancy_output(test)

