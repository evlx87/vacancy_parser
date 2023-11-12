from src.classes.class_parser import HeadHunterAPI
from src.file_saver import JSONSaver
from src.utils import get_hh_vacancies

keyword = input('Введите поисковой запрос: ')

hh_api = HeadHunterAPI()

vacancies_hh = get_hh_vacancies(hh_api.get_vacancies(keyword))

json_saver = JSONSaver()
json_saver.add(vacancies_hh)
