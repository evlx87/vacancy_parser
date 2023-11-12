class Vacancy:
    """Класс для работы с вакансиями"""

    def __init__(self, title, link, salary, requirements) -> None:
        """
        Инициализация объекта Vacancy
        Args:
            title (str): Название вакансии
            link (str): Ссылка на вакансию
            salary (int): Зарплата вакансии
            requirements (str): Требования к вакансии
        """
        self.title = title
        self.link = link
        self.salary = salary
        self.requirements = requirements

    def __lt__(self, other) -> bool:
        """
        Сравнение вакансий по зарплате: объект 1 < 2
        Args: other (Vacancy): Другой объект Vacancy для сравнения
        Returns: bool: True, если текущая вакансия имеет меньшую зарплату, иначе False
        """
        if other.salary is None:
            return False
        if self.salary is None:
            return True
        return self.salary < other.salary

    def __gt__(self, other) -> bool:
        """
        Сравнение вакансий по зарплате: объект 1 > 2
        Args: other (Vacancy): Другой объект Vacancy для сравнения
        Returns: bool: True, если текущая вакансия имеет большую зарплату, иначе False
        """
        return self.salary > other.salary

    @property
    def title(self) -> str:
        """
        Получение названия вакансии
        Returns: str: Название вакансии
        """
        return self.__title

    @title.setter
    def title(self, value: str) -> None:
        """
        Установка названия вакансии
        Args: value (str): Название вакансии
        """
        if isinstance(value, str):
            self.__title = value

    @property
    def link(self) -> str:
        """
        Получение ссылки на вакансию
        Returns: str: Ссылка на вакансию
        """
        return self.__link

    @link.setter
    def link(self, value: str) -> None:
        """
        Установка ссылки на вакансию
        Args: value (str): Ссылка на вакансию
        """
        if isinstance(value, str) and value.startswith('http'):
            self.__link = value

    @property
    def salary(self) -> int:
        """
        Получение зарплаты вакансии
        Returns: int: Зарплата вакансии
        """
        return self.__salary

    @salary.setter
    def salary(self, value: int) -> None:
        """
        Установка зарплаты вакансии
        Args: value (int): Зарплата вакансии
        """
        if isinstance(value, int):
            self.__salary = value
        if value in ('null', '0'):
            self.__salary = 0

    @property
    def requirements(self) -> str:
        """
        Получение требований к вакансии
        Returns: str: Требования к вакансии
        """
        return self.__requirements

    @requirements.setter
    def requirements(self, value: str) -> None:
        """
        Установка требований к вакансии
        Args: value (str): Требования к вакансии
        """
        if isinstance(value, str):
            self.__requirements = value
