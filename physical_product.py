from product import Product
from can_be_shipped import CanBeShipped

class PhysicalProduct(Product):
    def __init__(self, product_id, name, price, stock, weight):
        super().__init__(product_id, name, price, stock)
        self.weight = weight
        if self.weight < 0:
            raise ValueError("Weight cannot be negative.")

    def display_information(self):
        super().display_information()
        print(f"Weight: {self.weight:.2f} kg")

    def get_fufillment_method(self):
        return "This product requires physical shipping."

    def calculate_shipping_cost(self):
        shipping_rate = 5.00
        return self.weight * shipping_rate

CanBeShipped.register(PhysicalProduct)