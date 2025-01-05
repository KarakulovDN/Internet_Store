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
        products=["Samsung Galaxy S23 Ultra", "Iphone 15", "Xiaomi Redmi"
                                                           " Note 11"]
    )


@pytest.fixture()
def category_tv() -> Any:
    return Category(
        name="Телевизоры",
        description="Современный телевизор, который позволяет наслаждаться"
                    " просмотром, станет вашим другом и помощником",
        products=["Samsung", "Xiaomi", "Toshiba"]
    )
