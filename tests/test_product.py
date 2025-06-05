import pytest
from src.oop import Product, Smartphone, LawnGrass, Category


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


def test_product_str():
    product = Product("Test Product", "Test Description", 100.0, 10)
    assert str(product) == "Test Product, 100.0 руб. Остаток: 10"


def test_add_products():
    product1 = Product("Product1", "Desc1", 100.0, 2)
    product2 = Product("Product2", "Desc2", 200.0, 3)
    assert product1 + product2 == (100.0 * 2) + (200.0 * 3)


def test_add_valid_product(sample_smartphone, sample_category):
    initial_count = len(sample_category._Category__products)
    sample_category.add_product(sample_smartphone)
    assert len(sample_category._Category__products) == initial_count + 1
    assert sample_smartphone in sample_category._Category__products


def test_add_duplicate_product(sample_smartphone, sample_category):
    sample_category.add_product(sample_smartphone)
    initial_quantity = sample_smartphone.quantity
    duplicate = Smartphone(
        name=sample_smartphone.name,
        description="New description",
        price=sample_smartphone.price + 1000,
        quantity=5,
        efficiency="High",
        model="New Model",
        memory=512,
        color="Black"
    )
    sample_category.add_product(duplicate)
    assert len(sample_category._Category__products) == 1
    assert sample_category._Category__products[0].quantity == initial_quantity + duplicate.quantity
    assert sample_category._Category__products[0].price == duplicate.price


def test_add_invalid_type(sample_category):
    with pytest.raises(TypeError, match="Можно добавлять только объекты класса Product или его наследников"):
        sample_category.add_product("invalid product string")

    with pytest.raises(TypeError):
        sample_category.add_product(12345)

    with pytest.raises(TypeError):
        sample_category.add_product({"name": "Not a product"})


def test_add_different_product_types(sample_smartphone, sample_lawn_grass, sample_category):
    sample_category.add_product(sample_smartphone)
    sample_category.add_product(sample_lawn_grass)
    assert len(sample_category._Category__products) == 2
    assert isinstance(sample_category._Category__products[0], Smartphone)
    assert isinstance(sample_category._Category__products[1], LawnGrass)


def test_product_count_updates(sample_smartphone, sample_category):
    initial_count = Category.product_count
    sample_category.add_product(sample_smartphone)
    assert Category.product_count == initial_count + 1


@pytest.fixture
def sample_products(sample_smartphone, sample_lawn_grass):
    return [sample_smartphone, sample_lawn_grass]


def test_category_creation(sample_products):
    category = Category("Test", "Test desc", sample_products)
    assert len(category._Category__products) == len(sample_products)
    assert all(isinstance(p, Product) for p in category._Category__products)


def test_products_property(sample_category, sample_smartphone):
    sample_category.add_product(sample_smartphone)
    products_str = sample_category.products
    assert sample_smartphone.name in products_str
    assert str(sample_smartphone.price) in products_str
    assert str(sample_smartphone.quantity) in products_str


def test_str_representation(sample_category):
    assert "количество продуктов" in str(sample_category)


@pytest.fixture
def sample_smartphone():
    return Smartphone(
        name="Test Phone",
        description="Test Desc",
        price=10000,
        quantity=5,
        efficiency="High",
        model="X100",
        memory=256,
        color="Black"
    )


@pytest.fixture
def sample_lawn_grass():
    return LawnGrass(
        name="Test Grass",
        description="Test Desc",
        price=500,
        quantity=100,
        country="Russia",
        germination_period="14 дней",
        color="Green"
    )


@pytest.fixture
def sample_category():
    return Category("Test Category", "Test Description", [])


def test_mixin_logging(capsys):
    # Clear any previous output
    capsys.readouterr()
    
    # Create product and capture output
    product = Product("Test", "Description", 100.0, 5)
    captured = capsys.readouterr()
    
    # Check the output
    expected = "Создан объект класса Product с параметрами: Test, Description, 100.0, 5"
    assert expected in captured.out


def test_product_inheritance():
    product = Product("Test", "Description", 100.0, 5)
    assert isinstance(product, Product)
    assert hasattr(product, 'name')
    assert hasattr(product, 'description')
    assert hasattr(product, 'price')
    assert hasattr(product, 'quantity')
    assert hasattr(product, '__str__')
    assert hasattr(product, '__add__')
