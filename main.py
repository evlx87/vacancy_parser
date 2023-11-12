from src.utils import parser_run

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
        print("Мы работаем над этим")
    elif user_choice == "3":
        print("До свидания.")
    else:
        print("Вы ввели недопустимое значение. Попробуйте выбрать снова.")
        main()


if __name__ == '__main__':
    main()
