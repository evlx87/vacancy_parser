from src.classes.class_vacancy import Vacancy


def test_lt():
    vacancy1 = Vacancy(
        "Title 1",
        "http://example.com/vacancy1",
        1000,
        "Requirements 1")
    vacancy2 = Vacancy(
        "Title 2",
        "http://example.com/vacancy2",
        2000,
        "Requirements 2")
    assert vacancy1 < vacancy2
    assert not vacancy2 < vacancy1


def test_gt():
    vacancy1 = Vacancy(
        "Title 1",
        "http://example.com/vacancy1",
        1000,
        "Requirements 1")
    vacancy2 = Vacancy(
        "Title 2",
        "http://example.com/vacancy2",
        2000,
        "Requirements 2")
    assert vacancy2 > vacancy1
    assert not vacancy1 > vacancy2


def test_title():
    vacancy = Vacancy(
        "Title",
        "http://example.com/vacancy",
        1000,
        "Requirements")
    assert vacancy.title == "Title"
    vacancy.title = "New Title"
    assert vacancy.title == "New Title"


def test_link():
    vacancy = Vacancy(
        "Title",
        "http://example.com/vacancy",
        1000,
        "Requirements")
    assert vacancy.link == "http://example.com/vacancy"
    vacancy.link = "http://example.com/new_vacancy"
    assert vacancy.link == "http://example.com/new_vacancy"


def test_salary():
    vacancy = Vacancy(
        "Title",
        "http://example.com/vacancy",
        1000,
        "Requirements")
    assert vacancy.salary == 1000
    vacancy.salary = 2000
    assert vacancy.salary == 2000
    vacancy.salary = "null"
    assert vacancy.salary == 0
