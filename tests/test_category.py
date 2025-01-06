from typing import Any


def test_category_smart(category_smart: Any) -> Any:
    assert category_smart.name == "Смартфоны"
    assert (category_smart.description ==
            "Смартфоны, как средство не только коммуникации, но и"
            " получения дополнительных функций для удобства жизни")
    assert category_smart.products == ["Samsung Galaxy S23 Ultra",
                                       "Iphone 15", "Xiaomi Redmi Note 11"]


def test_category_tv(category_tv: Any) -> Any:
    assert category_tv.name == "Телевизоры"
    assert (category_tv.description ==
            "Современный телевизор, который позволяет"
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
