class Product:
    def __init__(self, name: str, description: str, price: float, quantity: int):
        self.name = name
        self.description = description
        self.price = price
        self.quantity = quantity


class Category:
    # Атрибуты класса для общего количества категорий и товаров
    total_categories = 0
    total_products = 0

    def __init__(self, name: str, description: str, products=None):
        self.name = name
        self.description = description
        self.products: list[Product] = products if products else []

        # Увеличиваем общее количество категорий при создании объекта
        Category.total_categories += 1

    def add_product(self, product: Product):
        """Добавляет продукт в категорию и обновляет счетчик товаров."""
        self.products.append(product)
        # Обновляем общее количество товаров во всех категориях
        Category.total_products += 1
