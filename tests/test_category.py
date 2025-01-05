from typing import Any


def test_category_smart(category_smart: Any) -> Any:
    assert category_smart.name == "Смартфоны"
    assert (category_smart.description ==
            "Смартфоны, как средство не только коммуникации, но и"
            " получения дополнительных функций для удобства жизни")
    assert category_smart.products == ["Samsung Galaxy S23 Ultra",
                                       "Iphone 15",
                                       "Xiaomi Redmi Note 11"]


def test_category_tv(category_tv: Any) -> Any:
    assert category_tv.name == "Телевизоры"
    assert (category_tv.description ==
            "Современный телевизор, который позволяет"
            " наслаждаться просмотром, станет вашим другом и помощником")
    assert category_tv.products == ["Samsung", "Xiaomi", "Toshiba"]


def test_category_count_tv(category_tv: Any) -> Any:
    assert len(category_tv.products) == 3
    assert category_tv.category_count == 3


def test_category_count_smart(category_smart: Any) -> Any:
    assert len(category_smart.products) == 3
    assert category_smart.category_count == 4
