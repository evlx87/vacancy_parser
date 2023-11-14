import json

from src.classes.class_vacancy import Vacancy
from src.utils import parser_run, get_vacancies_from_json

print("Программа поиска вакансий запущена.")


def main():
    user_choice = input("===================\n"
                        "Что вы хотите сделать:\n"
                        "1 - Запустить поиск вакансий на порталах HH и SJ\n"
                        "2 - Просмотреть вакансии загруженные в JSON файл\n"
                        "3 - Выйти из программы\n"
                        "Ваш выбор: ")

    if user_choice == "1":
        parser_run()
        main()
    elif user_choice == "2":
        with open('data/vacancy.json', 'r', encoding='utf-8') as f:
            list_vacancy = json.load(f)

        vacancies = [Vacancy(
            title=v['title'],
            link=v['link'],
            salary=v['salary'] if v.get('salary') else 0,
            requirements=v['requirements'])
            for v in list_vacancy]

        get_vacancies_from_json(vacancies)

    elif user_choice == "3":
        print("До свидания.")
    else:
        print("Вы ввели недопустимое значение. Попробуйте выбрать снова.")
        main()


if __name__ == '__main__':
    main()
