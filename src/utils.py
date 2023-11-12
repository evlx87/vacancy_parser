from src.classes.class_api import HeadHunterAPI
from src.file_saver import JSONSaver


def get_hh_vacancies(vacancy: list[dict]) -> list[dict]:
    """Форматирование объектов hh.ru"""
    vacancy_object = [{
        'title': item['name'],
        'link': item['alternate_url'],
        'salary': item['salary']['from'] if item.get('salary') else '0',
        'requirements': item['snippet']['requirement']
    } for item in vacancy]
    return vacancy_object


def parser_run():
    keyword = input('Введите поисковой запрос: ')
    hh_api = HeadHunterAPI()

    vacancies_hh = get_hh_vacancies(hh_api.get_vacancies(keyword))

    json_saver = JSONSaver()
    json_saver.add(vacancies_hh)

    print(f"Поиск вакансий по запросу '{keyword}' завершен.\n"
          f"Найдено {None} вакансий\n"
          f"Данные успешно загружены в vacancy.json")
