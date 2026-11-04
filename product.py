from abc import ABC, abstractmethod

class Product(ABC):

    def __init__(self, product_id, name, price, stock):
        self.product_id = product_id
        self.name = name
        self.price = float(price)
        self.stock = int(stock)

        if self.price < 0:
            raise ValueError("Price cannot be negative.")
        if self.stock < 0:
            raise ValueError("Stock cannot be negative.")

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

    @abstractmethod
    def get_fufillment_method(self):
        pass