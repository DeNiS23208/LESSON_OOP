from abc import ABC, abstractmethod


class CreationLogger:
    """Миксин для логирования создания объектов."""

    def __init__(self, *args, **kwargs):
        class_name = self.__class__.__name__
        print(f"Создан объект класса {class_name} с параметрами: {args}, {kwargs}")
        super().__init__(*args, **kwargs)


class BaseProduct(ABC):
    """Абстрактный базовый класс для всех товаров."""

    def __init__(self, name: str, description: str, price: float, quantity: int):
        self.name = name
        self.description = description
        self._price = price
        self.quantity = quantity

    @abstractmethod
    def __str__(self):
        pass

    @classmethod
    @abstractmethod
    def new_product(cls, product_info: dict):
        pass


class Product(CreationLogger, BaseProduct):
    """Класс продукта с базовым функционалом."""

    def __init__(self, name: str, description: str, price: float, quantity: int):
        if quantity == 0:
            raise ValueError("Товар с нулевым количеством не может быть добавлен")
        super().__init__(name, description, price, quantity)

    def __str__(self):
        return f"{self.name}, {self.price} руб. Остаток: {self.quantity} шт."

    def __add__(self, other):
        """Складывает только объекты одного типа по их общей стоимости."""
        if isinstance(other, self.__class__):
            return (self.price * self.quantity) + (other.price * other.quantity)
        raise TypeError("Сложение возможно только между объектами одного класса.")

    @property
    def price(self):
        return self._price

    @price.setter
    def price(self, value: float):
        if value <= 0:
            print("Цена не может быть отрицательной или нулевой")
        else:
            self._price = value

    @classmethod
    def new_product(cls, product_info: dict):
        return cls(
            product_info["name"],
            product_info["description"],
            product_info["price"],
            product_info["quantity"],
        )


class Smartphone(Product):
    """Класс смартфона с дополнительными параметрами."""

    def __init__(
        self, name, description, price, quantity, efficiency, model, memory, color
    ):
        super().__init__(name, description, price, quantity)
        self.efficiency = efficiency
        self.model = model
        self.memory = memory
        self.color = color

    def __str__(self):
        return (
            f"{self.name} ({self.model}, "
            f"{self.color}, {self.memory}GB) - {self.price} руб. Остаток: {self.quantity} шт."
        )


class LawnGrass(Product):
    """Класс газонной травы с дополнительными параметрами."""

    def __init__(
        self, name, description, price, quantity, country, germination_period, color
    ):
        super().__init__(name, description, price, quantity)
        self.country = country
        self.germination_period = germination_period
        self.color = color

    def __str__(self):
        return (
            f"{self.name} ({self.color}, {self.germination_period},"
            f"{self.country}) - {self.price} руб. Остаток: {self.quantity} шт."
        )


class Category:
    """Класс для хранения и работы с категориями товаров."""

    total_categories = 0
    total_products = 0

    def __init__(self, name: str, description: str, products=None):
        self.name = name
        self.description = description
        self._products = products if products else []

        Category.total_categories += 1
        Category.total_products += len(self._products)

    def __str__(self):
        return f"{self.name}, количество продуктов: {len(self._products)}"

    def add_product(self, product: Product):
        """Добавляет продукт в категорию и обновляет счетчик товаров."""
        if isinstance(product, Product):
            self._products.append(product)
            Category.total_products += 1
        else:
            raise TypeError("Можно добавлять только объекты типа Product.")

    def middle_price(self):
        try:
            return sum(product.price for product in self._products) / len(
                self._products
            )
        except ZeroDivisionError:
            return 0

    @property
    def products(self):
        return self._products

    @property
    def product_count(self):
        return len(self._products)

    @classmethod
    def category_count(cls):
        return cls.total_categories

    @classmethod
    def total_product_count(cls):
        return cls.total_products
