import pytest
from src.oop import Category, Product


@pytest.fixture()
def category_smartphones():
    product = Product("Samsung Galaxy S23 Ultra", "256GB, Серый цвет, 200MP камера", 180000.0, 5)
    return Category("Смартфоны",
                    "Смартфоны, как средство не только коммуникации, но и получения дополнительных функций для удобства жизни",
                    [product])


@pytest.fixture()
def category_tv():
    product = Product("55\" QLED 4K", "Фоновая подсветка", 123000.0, 7)
    return Category("Телевизоры",
                    "Современный телевизор, который позволяет наслаждаться просмотром, станет вашим другом и помощником",
                    [product])


def test_smartphones(category_smartphones):
    assert category_smartphones.name == "Смартфоны"
    assert category_smartphones.description == "Смартфоны, как средство не только коммуникации, но и получения дополнительных функций для удобства жизни"
    assert len(category_smartphones._Category__products) == 1
    product = category_smartphones._Category__products[0]
    assert product.name == "Samsung Galaxy S23 Ultra"
    assert product.description == "256GB, Серый цвет, 200MP камера"
    assert product.price == 180000.0
    assert product.quantity == 5


def test_tv(category_tv):
    assert category_tv.name == "Телевизоры"
    assert category_tv.description == "Современный телевизор, который позволяет наслаждаться просмотром, станет вашим другом и помощником"
    assert len(category_tv._Category__products) == 1
    product = category_tv._Category__products[0]
    assert product.name == "55\" QLED 4K"
    assert product.description == "Фоновая подсветка"
    assert product.price == 123000.0
    assert product.quantity == 7


def test_category_str(sample_products):
    category = Category("Test Category", "Test Description", sample_products)
    total_quantity = sum(product.quantity for product in sample_products)
    assert str(category) == f"Test Category, количество продуктов: {total_quantity} шт."


@pytest.fixture
def sample_products():
    product1 = Product("Test Product 1", "Test Description 1", 100.0, 5)
    product2 = Product("Test Product 2", "Test Description 2", 200.0, 3)
    return [product1, product2]
