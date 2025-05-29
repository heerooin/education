import pytest
from src.oop import Category


@pytest.fixture()
def category_smartphones():
    return Category("Смартфоны",
                    "Смартфоны, как средство не только коммуникации, но и получения дополнительных функций для удобства жизни",
                    ["Samsung Galaxy S23 Ultra", "256GB, Серый цвет, 200MP камера", 180000.0, 5])


@pytest.fixture()
def category_tv():
    return Category("Телевизоры",
                    "Современный телевизор, который позволяет наслаждаться просмотром, станет вашим другом и помощником",
                    ["Телевизоры", "Современный телевизор, который позволяет наслаждаться просмотром, станет вашим другом и помощником"])

def test_smartphones(category_smartphones):
    assert category_smartphones.name == "Смартфоны"
    assert category_smartphones.description == "Смартфоны, как средство не только коммуникации, но и получения дополнительных функций для удобства жизни"
    assert category_smartphones.products == ["Samsung Galaxy S23 Ultra",
                                             "256GB, Серый цвет, 200MP камера", 180000.0, 5]


def test_tv(category_tv):
    assert category_tv.name == "Телевизоры"
    assert category_tv.description == "Современный телевизор, который позволяет наслаждаться просмотром, станет вашим другом и помощником"
    assert category_tv.products == ["Телевизоры",
                                    "Современный телевизор, который позволяет наслаждаться просмотром, станет вашим другом и помощником"]


def test_category_str(self, sample_products):
    category = Category("Test Category", "Test Description", sample_products)
    assert str(category) == "Test Category, количество продуктов: 2 шт."
