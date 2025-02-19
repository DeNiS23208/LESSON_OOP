class Product:
    def __init__(self, name: str, description: str, price: float, quantity: int):
        self.name = name
        self.description = description
        self._price = price  # Приватный атрибут для цены
        self.quantity = quantity

    def __str__(self):
        """Строковое представление товара"""
        return f"{self.name}, {self._price} руб. Остаток: {self.quantity} шт."

    def __add__(self, other):
        """Складывает два продукта по их общей стоимости (цена * количество)."""
        if isinstance(other, Product):
            return (self._price * self.quantity) + (other._price * other.quantity)

        raise TypeError("Сложение возможно только между объектами Product.")

    @property
    def price(self):
        """Геттер для атрибута цены."""
        return self._price

    @price.setter
    def price(self, value: float):
        """Сеттер для атрибута цены с проверкой на отрицательное значение."""
        if value <= 0:
            print("Цена не должна быть нулевая или отрицательная")
        else:
            self._price = value

    @classmethod
    def new_product(cls, product_info: dict):
        """Класс-метод для создания нового товара из словаря."""
        return cls(
            product_info["name"],
            product_info["description"],
            product_info["price"],
            product_info["quantity"],
        )


class Smartphone(Product):
    def __init__(
        self,
        name: str,
        description: str,
        price: float,
        quantity: int,
        efficiency: str,
        model: str,
        memory: int,
        color: str,
    ):
        super().__init__(name, description, price, quantity)
        self.efficiency = efficiency
        self.model = model
        self.memory = memory
        self.color = color

    def __str__(self):
        return (
            f"{self.name} ({self.model}), {self.memory}GB, {self.color}, "
            f"{self._price} руб. Остаток: {self.quantity} шт."
        )

    def __add__(self, other):
        if isinstance(other, Smartphone) and type(self) == type(other):
            return (self._price * self.quantity) + (other._price * other.quantity)
        raise TypeError(
            "Сложение возможно только между объектами одного типа (Smartphone)."
        )


class LawnGrass(Product):
    def __init__(
        self,
        name: str,
        description: str,
        price: float,
        quantity: int,
        country: str,
        germination_period: int,
        color: str,
    ):
        super().__init__(name, description, price, quantity)
        self.country = country
        self.germination_period = germination_period
        self.color = color

    def __str__(self):
        return (
            f"{self.name} ({self.country}), {self.color}, "
            f"Прорастание: {self.germination_period} дней, "
            f"{self._price} руб. Остаток: {self.quantity} шт."
        )

    def __add__(self, other):
        if isinstance(other, LawnGrass) and type(self) == type(other):
            return (self._price * self.quantity) + (other._price * other.quantity)
        raise TypeError(
            "Сложение возможно только между объектами одного типа (LawnGrass)."
        )


class Category:
    # Атрибуты класса для общего количества категорий и товаров
    total_categories = 0
    total_products = 0

    def __init__(self, name: str, description: str, products=None):
        self.name = name
        self.description = description
        # Приватный атрибут списка товаров
        self._products: list[Product] = products if products else []

        # Увеличиваем общее количество категорий при создании объекта
        Category.total_categories += 1

    def __str__(self):
        """Строковое представление категории"""
        total_quantity = sum(product.quantity for product in self._products)
        return f"{self.name}, количество продуктов: {total_quantity} шт."

    def add_product(self, product: Product):
        if not isinstance(product, Product):
            raise TypeError("Можно добавлять только объекты Product и его наследников.")
        self._products.append(product)
        Category.total_products += 1

    @property
    def products(self):
        """Геттер для списка товаров в категории."""
        return self._products

    @property
    def product_count(self):
        """Возвращает количество товаров в категории."""
        return len(self._products)

    def get_products(self):
        """Возвращает список товаров в категории в виде строк"""
        return [str(product) for product in self._products]
