import pytest
from src.oop import Product


@pytest.fixture()
def product_samsung():
    return Product("Samsung Galaxy S23 Ultra", "256GB, Серый цвет, 200MP камера", 180000.0, 5)


@pytest.fixture()
def product_iphone():
    return Product("Iphone 15", "512GB, Gray space", 210000.0, 8)


@pytest.fixture()
def product_xiaomi():
    return Product("Xiaomi Redmi Note 11", "1024GB, Синий", 31000.0, 14)


def test_samsung(product_samsung):
    assert product_samsung.name == "Samsung Galaxy S23 Ultra"
    assert product_samsung.description == "256GB, Серый цвет, 200MP камера"
    assert product_samsung.price == 180000.0
    assert product_samsung.quantity == 5


def test_iphone(product_iphone):
    assert product_iphone.name == "Iphone 15"
    assert product_iphone.description == "512GB, Gray space"
    assert product_iphone.price == 210000.0
    assert product_iphone.quantity == 8


def test_xiaomi(product_xiaomi):
    assert product_xiaomi.name == "Xiaomi Redmi Note 11"
    assert product_xiaomi.description == "1024GB, Синий"
    assert product_xiaomi.price == 31000.0
    assert product_xiaomi.quantity == 14

def test_product_creation():
    product = Product("Телефон", "Смартфон", 50000.0, 10)
    assert product.name == "Телефон"
    assert product.description == "Смартфон"
    assert product.price == 50000.0
    assert product.quantity == 10

def test_price_setter_positive():
    product = Product("Ноутбук", "Игровой", 100000.0, 5)
    product.price = 90000.0
    assert product.price == 90000.0

def test_price_setter_negative(capsys):
    product = Product("Планшет", "Графический", 30000.0, 3)
    product.price = -5000.0
    captured = capsys.readouterr()
    assert "Цена не должна быть нулевая или отрицательная" in captured.out
    assert product.price == 30000.0

def test_new_product_classmethod():
    product_data = {
        "name": "Монитор",
        "description": "4K",
        "price": 25000.0,
        "quantity": 7
    }
    product = Product.new_product(product_data)
    assert product.name == "Монитор"
    assert product.price == 25000.0
    assert product.quantity == 7

def test_private_price_access():
    product = Product("Клавиатура", "Механическая", 5000.0, 15)
    with pytest.raises(AttributeError):
        print(product.__price)
