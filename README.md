# Интернет-магазин
/## Описание проекта

Класс __Product__ с параметрами:
* name
* description
* price
* quantity

Класс __Category__ с параметрами:
* name
* description
* products

## Структура проекта:

    ├──  data 
    │   └── products.json   
    ├── src   
    │   ├── category.py   
    │   └── product.py  
    ├── tests
    │   ├── test_product.py
    │   ├── test_category.py
    │   └── conftest.py 
    │   
    └── main.py

__data__\ — папка содержит данные товаров магазина (база данных).

__src__\ — папка содержит файлы с функциями проекта.
* category.py - модуль, в котором реализован класс с категориями.
* product.py - модуль, в котором реализован класс с продуктами.

__tests__\ — папка с тестами функционала проекта.
* test_product.py - модуль, в котором происходит тестирование модуля product.
* test_category.py - модуль, в котором происходит тестирование модуля category.
* confitest.py - содержит фикстуры для тестов
