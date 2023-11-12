def get_hh_vacancies(vacancy: list[dict]) -> list[dict]:
    """Форматирование объектов hh.ru"""
    vacancy_object = [{
        'title': item['name'],
        'link': item['alternate_url'],
        'salary': item['salary']['from'] if item.get('salary') else '0',
        'requirements': item['snippet']['requirement']
    } for item in vacancy]
    return vacancy_object
