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


# Тест для абстрактного класса BaseProduct и создания продукта с использованием new_product
def test_new_product_creation():
    product_info = {
        "name": "Samsung Galaxy S23 Ultra",
        "description": "256GB, Серый цвет, 200MP камера",
        "price": 180000.0,
        "quantity": 5,
    }

    # Проверяем, что new_product создает объект класса Product
    product = Product.new_product(product_info)
    assert isinstance(product, Product)
    assert product.name == "Samsung Galaxy S23 Ultra"
    assert product.price == 180000.0
    assert product.quantity == 5


# Тест для создания объекта Product и проверки его атрибутов
def test_product_creation():
    product = Product(
        "Samsung Galaxy S23 Ultra", "256GB, Серый цвет, 200MP камера", 180000.0, 5
    )

    # Проверяем правильность инициализации атрибутов
    assert product.name == "Samsung Galaxy S23 Ultra"
    assert product.description == "256GB, Серый цвет, 200MP камера"
    assert product.price == 180000.0
    assert product.quantity == 5


# Тест для создания объекта Category и проверки его атрибутов
def test_category_creation():
    product1 = Product(
        "Samsung Galaxy S23 Ultra", "256GB, Серый цвет, 200MP камера", 180000.0, 5
    )
    product2 = Product("Iphone 15", "512GB, Gray space", 210000.0, 8)

    category = Category("Смартфоны", "Описание смартфонов", [product1, product2])

    # Проверяем правильность инициализации атрибутов категории
    assert category.name == "Смартфоны"
    assert category.description == "Описание смартфонов"
    assert len(category.products) == 2
    assert category.product_count == 2


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


@pytest.fixture
def product1():
    return Product(
        "Samsung Galaxy S23 Ultra", "256GB, Серый цвет, 200MP камера", 180000.0, 5
    )


@pytest.fixture
def product2():
    return Product("Iphone 15", "512GB, Gray space", 210000.0, 8)


@pytest.fixture
def category(product1):
    return Category("Смартфоны", "Описание категории", [product1])


def test_price_setter(product1):
    """Проверка сеттера цены с валидными и невалидными значениями"""
    product1.price = 50000  # Должно измениться
    assert product1.price == 50000

    product1.price = -1000  # Должно остаться 50000
    assert product1.price == 50000


def test_new_product_method():
    """Проверка метода new_product"""
    data = {
        "name": "Xiaomi Redmi Note 11",
        "description": "1024GB, Синий",
        "price": 31000.0,
        "quantity": 14,
    }
    new_product = Product.new_product(data)
    assert new_product.name == "Xiaomi Redmi Note 11"
    assert new_product.price == 31000.0


def test_get_products(category, product2):
    """Проверка метода get_products"""
    expected_output = ["Samsung Galaxy S23 Ultra, 180000.0 руб. Остаток: 5 шт."]
    assert [str(p) for p in category.products] == expected_output

    category.add_product(product2)
    expected_output.append("Iphone 15, 210000.0 руб. Остаток: 8 шт.")
    assert [str(p) for p in category.products] == expected_output


def test_product_str():
    """Тест строкового представления товара"""
    product = Product("Хлеб", "Свежий ржаной хлеб", 50, 20)
    assert str(product) == "Хлеб, 50 руб. Остаток: 20 шт."


def test_product_addition():
    """Тест сложения товаров"""
    p1 = Product("Молоко", "Свежая фермерская продукция", 100, 10)
    p2 = Product("Сыр", "Натуральный сыр", 200, 2)
    assert p1 + p2 == 1400  # 100 * 10 + 200 * 2 = 1400


def test_category_get_products():
    """Тест метода get_products()"""
    p1 = Product("Яблоко", "Красное яблоко", 30, 5)
    p2 = Product("Груша", "Сладкая груша", 40, 7)
    category = Category("Фрукты", "Свежие фрукты", [p1, p2])

    assert [str(p) for p in category.products] == [
        "Яблоко, 30 руб. Остаток: 5 шт.",
        "Груша, 40 руб. Остаток: 7 шт.",
    ]


def test_product_addition_type_error():
    """Тест ошибки при сложении продукта с не-Product объектом"""
    p1 = Product("Молоко", "Свежая фермерская продукция", 100, 10)
    with pytest.raises(TypeError):
        p1 + 10  # Должно вызывать TypeError


def test_product_quantity_zero():
    """Проверка, что при нулевом количестве вызывается ValueError"""
    with pytest.raises(
        ValueError, match="Товар с нулевым количеством не может быть добавлен"
    ):
        Product("Бракованный товар", "Неверное количество", 1000.0, 0)


def test_middle_price():
    """Проверка метода middle_price()"""
    product1 = Product("Товар 1", "Описание 1", 100.0, 2)
    product2 = Product("Товар 2", "Описание 2", 200.0, 3)
    category = Category("Категория 1", "Описание", [product1, product2])

    assert category.middle_price() == 150.0  # (100*2 + 200*3) / 5 = 150


def test_middle_price_empty():
    """Проверка middle_price() для пустой категории"""
    empty_category = Category("Пустая категория", "Описание", [])
    assert empty_category.middle_price() == 0
