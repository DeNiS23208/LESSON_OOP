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
        """Добавляет продукт в категорию и обновляет счетчик товаров."""
        if isinstance(product, Product):  # Проверка, что передан объект Product
            self._products.append(product)
            # Обновляем общее количество товаров во всех категориях
            Category.total_products += 1
        else:
            raise ValueError("Товар должен быть объектом класса Product.")

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
