# test_models.py
import pytest

from classes import Category, Product


@pytest.fixture(autouse=True)
def reset_category_counters():
    """Перед каждым тестом сбрасываем счётчики категорий и продуктов"""
    Category.total_categories = 0
    Category.total_products = 0


def test_product_initialization():
    """Тестирование инициализации объекта Product"""
    product = Product(
        "Samsung Galaxy S23 Ultra", "256GB, Серый цвет, 200MP камера", 180000.0, 5
    )

    assert product.name == "Samsung Galaxy S23 Ultra"
    assert product.description == "256GB, Серый цвет, 200MP камера"
    assert product.price == 180000.0
    assert product.quantity == 5


def test_category_initialization():
    """Тестирование инициализации объекта Category"""
    category = Category("Смартфоны", "Категория для смартфонов")

    assert category.name == "Смартфоны"
    assert category.description == "Категория для смартфонов"
    assert len(category.products) == 0  # Категория создаётся пустой
    assert Category.total_categories == 1  # Должна быть 1 категория


def test_add_product():
    """Тестирование добавления продуктов в категорию"""
    category = Category("Смартфоны", "Категория для смартфонов")
    product = Product("iPhone 15", "512GB, Gray Space", 210000.0, 8)

    category.add_product(product)

    assert len(category.products) == 1
    assert Category.total_products == 1


def test_category_counts():
    """Тестирование общего количества категорий и продуктов"""
    category1 = Category("Смартфоны", "Категория для смартфонов")
    category2 = Category("Телевизоры", "Категория для телевизоров")

    product1 = Product("iPhone 15", "512GB, Gray Space", 210000.0, 8)
    product2 = Product("Samsung TV", "QLED 4K", 150000.0, 3)

    category1.add_product(product1)
    category2.add_product(product2)

    assert Category.total_categories == 2  # Две категории
    assert Category.total_products == 2  # Два продукта
