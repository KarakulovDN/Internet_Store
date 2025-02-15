from typing import Any

import pytest

from src.category import Category
from src.product import Product


def test_category_smart(category_smart: Any) -> Any:
    assert category_smart.name == "Смартфоны"
    assert (category_smart.description == "Смартфоны, как средство не только коммуникации, но и"
            " получения дополнительных функций для удобства жизни")
    assert category_smart.products == ["Samsung Galaxy S23 Ultra",
                                       "Iphone 15", "Xiaomi Redmi Note 11"]


def test_category_tv(category_tv: Any) -> Any:
    assert category_tv.name == "Телевизоры"
    assert (category_tv.description == "Современный телевизор, который позволяет"
            " наслаждаться просмотром, станет вашим другом и помощником")
    assert category_tv.products == ["Samsung", "Xiaomi", "Toshiba"]


def test_category_count_tv(category_tv: Any) -> Any:
    assert len(category_tv.products) == 3


def test_category_count_smart(category_smart: Any) -> Any:
    assert len(category_smart.products) == 3


def test_all_count(category_smart: Any, category_tv: Any) -> Any:
    assert len(category_smart.products) + len(category_tv.products) == 6


def test_product_smart(product_smart) -> Any:
    assert product_smart.name == "Samsung Galaxy S23 Ultra"
    assert product_smart.description == "256GB, Серый цвет, 200MP камера"
    assert product_smart.price == 180000.0
    assert product_smart.quantity == 5


def test_product_tv(product_tv) -> Any:
    assert product_tv.name == "55\" QLED 4K"
    assert product_tv.description == "Фоновая подсветка"
    assert product_tv.price == 123000.0
    assert product_tv.quantity == 7


def test_add_product_to_existing_list(product1_fixture: Product, product2_fixture: Product) -> None:
    """Проверяем работу метода add_product для случая, когда добавляется список продуктов и продукт в конструктор."""
    test_category = Category(name="Продукты", description="Товары первой необходимости", products=[product1_fixture])
    test_category.add_product(product2_fixture)
    assert test_category.products == ["Молоко, 500.0 руб. Остаток: 5 шт.", "Хлеб, 100.0 руб. Остаток: 3 шт."]


def test_add_product_if_invalid_arg(product1_fixture: Product) -> None:
    """Проверяем работу метода add_product для случая, когда добавляется не экземпляр класса Product."""
    test_category = Category(name="Продукты", description="Товары первой необходимости", products=[product1_fixture])
    with pytest.raises(TypeError):
        test_category.add_product("Not product")


def test_category_getter() -> None:
    """Проверяем работу геттера когда есть список продуктов."""
    product1 = Product(name="Ноутбук", description="Компьютеры", price=80000, quantity=15)
    product2 = Product(name="Смартфон", description="Телефоны", price=60000, quantity=10)
    category = Category(
        name="Электроника", description="Электроника и устройства для дома", products=[product1, product2]
    )
    expected_result = ["Ноутбук, 80000 руб. Остаток: 15 шт.", "Смартфон, 60000 руб. Остаток: 10 шт."]
    assert category.products == expected_result


def test_products_property_empty() -> None:
    """Проверяем работу геттера когда список продуктов пустой."""
    category = Category(name="Книги", description="Книги всех жанров")
    assert category.products == []
