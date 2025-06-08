from abc import ABC, abstractmethod


class BaseProduct(ABC):
    @property
    @abstractmethod
    def name(self) -> str:
        pass

    @property
    @abstractmethod
    def description(self) -> str:
        pass

    @property
    @abstractmethod
    def price(self) -> float:
        pass

    @property
    @abstractmethod
    def quantity(self) -> int:
        pass

    @abstractmethod
    def __str__(self) -> str:
        pass

    @abstractmethod
    def __add__(self, other) -> float:
        pass


class MixIn:
    def __init__(self, *args, **kwargs):
        class_name = self.__class__.__name__
        params = []
        if args:
            params.extend([str(arg) for arg in args])
        if kwargs:
            params.extend([f"{k}={v}" for k, v in kwargs.items()])
        params_str = ", ".join(params)
        print(f"Создан объект класса {class_name} с параметрами: {params_str}")


class Product(MixIn):
    name: str
    description: str
    price: float
    quantity: int

    def __init__(self, name, description, price, quantity):
        self.name = name
        self.description = description
        self.__price = price
        self.quantity = quantity
        if quantity == 0:
            raise  ValueError
            print("Товар с нулевым количеством не может быть добавлен")

    def __str__(self):
        return f"{self.name}, {self.__price} руб. Остаток: {self.quantity}"

    def __add__(self, other):
        try:
            if type(self) is type(other):
                return (self.price * self.quantity) + (other.price * other.quantity)
        except TypeError:
            print("Ошибка")

    @property
    def price(self) -> float:
        return self.__price

    @price.setter
    def price(self, new_price: float) -> None:
        if new_price > 0:
            self.__price = new_price
        else:
            print("Цена не должна быть нулевая или отрицательная")

    @classmethod
    def new_product(cls, product_data: dict) -> 'Product':
        return cls(
            name=product_data.get('name'),
            description=product_data.get('description'),
            price=product_data.get('price'),
            quantity=product_data.get('quantity')
        )


class Category:
    name: str
    description: str
    products: list[Product]

    product_count = 0
    category_count = 0

    def __init__(self, name, description, products):
        self.name = name
        self.description = description
        self.__products = []
        for product in products:
            self.add_product(product)
        Category.category_count += 1

    def __str__(self):
        total_quantity = sum(product.quantity for product in self.__products)
        return f"{self.name}, количество продуктов: {total_quantity} шт."

    def add_product(self, product):
        if not isinstance(product, Product):
            raise TypeError("Можно добавлять только объекты класса Product или его наследников")
        
        # Check if product with same name exists
        for existing_product in self.__products:
            if existing_product.name == product.name:
                existing_product.quantity += product.quantity
                if product.price > existing_product.price:
                    existing_product.price = product.price
                return
        
        self.__products.append(product)
        Category.product_count += 1

    @property
    def products(self):
        products_info = []
        for product in self.__products:
            products_info.append(
                f"{product.name}, {product.price} руб. Остаток: {product.quantity} шт.")
        return "\n".join(products_info)

    def middle_price(self):
        try:
            if not self.__products:
                return 0
            total_price = sum(product.price * product.quantity for product in self.__products)
            total_quantity = sum(product.quantity for product in self.__products)
            return total_price / total_quantity
        except ZeroDivisionError:
            return 0


class Smartphone(BaseProduct, Product, MixIn):
    def __init__(self, name, description, price, quantity, efficiency, model, memory, color):
        super().__init__(name, description, price, quantity)
        self.efficiency = efficiency
        self.model = model
        self.memory = memory
        self.color = color

    def __str__(self):
        return f"{self.name}, {self.price} руб. Остаток: {self.quantity}"

    def __add__(self, other):
        if isinstance(other, Smartphone):
            return (self.price * self.quantity) + (other.price * other.quantity)
        raise TypeError("Можно складывать только объекты одного класса")


class LawnGrass(BaseProduct, Product, MixIn):
    def __init__(self, name, description, price, quantity, country, germination_period, color):
        super().__init__(name, description, price, quantity)
        self.country = country
        self.germination_period = germination_period
        self.color = color

    def __str__(self):
        return f"{self.name}, {self.price} руб. Остаток: {self.quantity}"

    def __add__(self, other):
        if isinstance(other, LawnGrass):
            return (self.price * self.quantity) + (other.price * other.quantity)
        raise TypeError("Можно складывать только объекты одного класса")


if __name__ == '__main__':
    try:
        product_invalid = Product("Бракованный товар", "Неверное количество", 1000.0, 0)
    except ValueError as e:
        print(
            "Возникла ошибка ValueError прерывающая работу программы при попытке добавить продукт с нулевым количеством")
    else:
        print("Не возникла ошибка ValueError при попытке добавить продукт с нулевым количеством")

    product1 = Product("Samsung Galaxy S23 Ultra", "256GB, Серый цвет, 200MP камера", 180000.0, 5)
    product2 = Product("Iphone 15", "512GB, Gray space", 210000.0, 8)
    product3 = Product("Xiaomi Redmi Note 11", "1024GB, Синий", 31000.0, 14)

    category1 = Category("Смартфоны", "Категория смартфонов", [product1, product2, product3])

    print(category1.middle_price())

    category_empty = Category("Пустая категория", "Категория без продуктов", [])
    print(category_empty.middle_price())