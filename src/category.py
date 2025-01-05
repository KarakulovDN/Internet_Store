class Category:
    name: str
    description: str
    products: list
    category_count = 0
    product_count = 0

    def __init__(self, name, description=None, products=None):
        self.name = name
        self.description = (
            description) if description else 'Описание категории отсутствует'
        self.products = products if products else []
        Category.category_count += 1
        Category.product_count += len(products)
