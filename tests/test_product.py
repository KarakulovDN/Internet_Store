from typing import Any


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
