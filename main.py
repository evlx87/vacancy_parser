from src.class_parser import HeadHunterAPI

keyword = input('Введите поисковой запрос: ')

# получение вакансий по запросу с API
hh_api = HeadHunterAPI()
print(hh_api.get_vacancies(keyword))
