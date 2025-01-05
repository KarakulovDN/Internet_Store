class Product:
    name: str
    description: str
    price: float
    quantity: int

    def __init__(self, name, description=None, price=None, quantity=None):
        self.name = name
        self.description = description if description else ('Описание к товару'
                                                            ' отсутствует')
        self.price = price if price else price
        self.quantity = quantity if quantity else quantity
