from typing import Any

from src.category import Category
from src.product import Product

import pytest


@pytest.fixture()
def product_smart() -> Any:
    return Product(
        name="Samsung Galaxy S23 Ultra",
        description="256GB, Серый цвет, 200MP камера",
        price=180000.0,
        quantity=5
    )


@pytest.fixture()
def product_tv() -> Any:
    return Product(
        name="55\" QLED 4K",
        description="Фоновая подсветка",
        price=123000.0,
        quantity=7
    )


@pytest.fixture()
def category_smart() -> Any:
    return Category(
        name="Смартфоны",
        description="Смартфоны, как средство не только коммуникации, но и"
                    " получения дополнительных функций для удобства жизни",
        products=["Samsung Galaxy S23 Ultra", "Iphone 15",
                  "Xiaomi Redmi Note 11"]
    )


@pytest.fixture()
def category_tv() -> Any:
    return Category(
        name="Телевизоры",
        description="Современный телевизор, который позволяет наслаждаться"
                    " просмотром, станет вашим другом и помощником",
        products=["Samsung", "Xiaomi", "Toshiba"]
    )


@pytest.fixture
def product1_fixture() -> Product:
    """Фикстура для тестирования инициализации экземпляров класса Product."""
    return Product(name="Молоко", description="Молоко коровье 3%", price=500.00, quantity=5)


@pytest.fixture
def product2_fixture() -> Product:
    """Фикстура для тестирования инициализации экземпляров класса Product."""
    return Product(name="Хлеб", description="Хлеб белый стандартный", price=100.00, quantity=3)


@pytest.fixture
def product3_fixture() -> Product:
    """Фикстура для тестирования инициализации экземпляров класса Product."""
    return Product(name="Яйца", description="Яйца 1С", price=500.00, quantity=2)


@pytest.fixture
def product4_fixture() -> Product:
    """Фикстура для тестирования инициализации экземпляров класса Product."""
    return Product(name="Шорты", description="Шорты мужские, размер 50", price=5000.00, quantity=2)


@pytest.fixture
def params_fixture() -> dict:
    """Фикстура для метода new_product класса Product."""
    return {
        "name": "Яйца",
        "description": "Яйца 1С",
        "price": 500.0,
        "quantity": 1,
    }


@pytest.fixture
def smartphone_params_fixture() -> dict:
    """Фикстура для создания нового экземпляра методом new_product."""
    return {
        "name": "Samsung Galaxy S23 Ultra",
        "description": "256GB, Серый цвет, 200MP камера",
        "price": 180000.0,
        "quantity": 5,
        "efficiency": 95.5,
        "model": "S23 Ultra",
        "memory": 256,
        "color": "Серый",
    }
@pytest.fixture
def category1_fixture() -> Category:
    """Фикстура для тестирования инициализации экземпляров класса Category."""
    return Category(
        name="Продукты",
        description="Товары первой необходимости",
        products=[
            Product("Молоко", "Молоко коровье 3%", 500.00, 5),
            Product("Хлеб", "Хлеб белый стандартный", 100.00, 3),
            Product("Яйца", "Яйца 1С", 500.00, 2),
        ],
    )