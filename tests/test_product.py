from typing import Any

from src.product import Product


def test_product_smart(product_smart: Any) -> Any:
    assert product_smart.name == "Samsung Galaxy S23 Ultra"
    assert product_smart.description == "256GB, Серый цвет, 200MP камера"
    assert product_smart.price == 180000.0
    assert product_smart.quantity == 5


def test_product_tv(product_tv: Any) -> Any:
    assert product_tv.name == "55\" QLED 4K"
    assert product_tv.description == "Фоновая подсветка"
    assert product_tv.price == 123000.0
    assert product_tv.quantity == 7


def test_product1_init(product1_fixture: Product) -> None:
    """Тестируем инициализацию экземпляра класса Product."""
    assert product1_fixture.name == "Молоко"
    assert product1_fixture.description == "Молоко коровье 3%"
    assert product1_fixture.price == 500.00


def test_product2_init(product2_fixture: Product) -> None:
    """Тестируем инициализацию экземпляра класса Product."""
    assert product2_fixture.name == "Хлеб"
    assert product2_fixture.description == "Хлеб белый стандартный"
    assert product2_fixture.price == 100.00


def test_product3_init(product3_fixture: Product) -> None:
    """Тестируем инициализацию экземпляра класса Product."""
    assert product3_fixture.name == "Яйца"
    assert product3_fixture.description == "Яйца 1С"
    assert product3_fixture.price == 500.00


def test_product4_init(product4_fixture: Product) -> None:
    """Тестируем инициализацию экземпляра класса Product."""
    assert product4_fixture.name == "Шорты"
    assert product4_fixture.description == "Шорты мужские, размер 50"
    assert product4_fixture.price == 5000.00


def test_product1_count(product1_fixture: Product) -> None:
    """Проверяем, что количество продуктов вычисляется правильно."""
    assert product1_fixture.quantity == 5


def test_product2_count(product2_fixture: Product) -> None:
    """Проверяем, что количество продуктов вычисляется правильно."""
    assert product2_fixture.quantity == 3


def test_product3_count(product3_fixture: Product) -> None:
    """Проверяем, что количество продуктов вычисляется правильно."""
    assert product3_fixture.quantity == 2


def test_product4_count(product4_fixture: Product) -> None:
    """Проверяем, что количество продуктов вычисляется правильно."""
    assert product4_fixture.quantity == 2


def test_new_product(params_fixture: dict) -> None:
    """Тестируем класс-метод new_product."""
    new_product = Product.new_product(params_fixture)
    assert new_product.name == "Яйца"
    assert new_product.description == "Яйца 1С"
    assert new_product.price == 500.0  # Цена не изменится, так как 120.0 < 150.0
    assert new_product.quantity == 3


def test_new_product_new_entry(params_fixture: dict) -> None:
    """Тестируем класс-метод new_product."""
    new_product = Product.new_product(params_fixture)
    assert new_product.name == "Яйца"
    assert new_product.description == "Яйца 1С"
    assert new_product.price == 500.0  # Цена останется такой же, так как это новый продукт
    assert new_product.quantity == 3


class TestProduct:
    """Класс для тестирования геттера и сеттера класса Product."""

    def test_price_getter(self) -> None:
        """Тестируем геттер."""
        # Создаем экземпляр продукта
        product = Product(name="Пармезан", description="Натуральные сыры", price=99.99, quantity=10)

        # Проверяем, что геттер возвращает правильное значение.
        assert product.price == 99.99

    def test_price_setter(self) -> None:
        """Тестируем сеттер."""
        # Создаем экземпляр продукта
        product1 = Product(name="Пармезан", description="Натуральные сыры", price=99.99, quantity=10)

        # Проверяем, что сеттер устанавливает правильное значение.
        product1.price = 120.00
        assert product1.price == 120.00


def test_product_str(product1_fixture: Product) -> None:
    """Тест для проверки метода __str__ класса Product."""
    assert str(product1_fixture) == "Молоко, 500.0 руб. Остаток: 5 шт."


def test_product_add(product1_fixture: Product, product2_fixture: Product) -> None:
    """Тест для проверки метода __add__ класса Product."""
    assert product1_fixture + product2_fixture == 2800.00
