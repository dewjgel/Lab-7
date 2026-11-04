class Product:
    def __init__(self, product_id, name, price, stock):
        self.product_id = product_id
        self.name = name
        self.price = float(price)
        self.stock = int(stock)

    def product_id(self):
        return self.product_id

    def name(self):
        return self.name

    def stock(self):
        return self.stock

    def update_stock(self, quantity):
        if not isinstance(quantity, int) or isinstance(quantity,bool):
            raise ValueError("Stock must be a whole number.")

        if quantity < 0:
            raise ValueError("Stock cannot be negative.")

        self.stock = quantity

    def display_information(self):
        print(f"Product ID: {self.product_id}")
        print(f"Name: {self.name}")
        print(f"Price: ${self.price:.2f}")
        print(f"Stock: {self.stock}")
        