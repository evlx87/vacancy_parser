from src.classes.class_parser import HeadHunterAPI
from src.classes.class_vacancy import Vacancy
from src.file_saver import JSONSaver

keyword = input('Введите поисковой запрос: ')

# Создание экземпляра класса для работы с API сайтов с вакансиями
hh_api = HeadHunterAPI()

# Получение вакансий с разных платформ
hh_vacancies = hh_api.get_vacancies(keyword)

# Создание экземпляра класса для работы с вакансиями
vacancy = Vacancy(
    "Разработчик Python (Support)",
    "https://hh.ru/vacancy/88640343",
    90000,
    "Требуемый опыт работы: 1–3 года")

# Сохранение информации о вакансиях в файл
json_saver = JSONSaver()
json_saver.add(vacancy.to_dict())

