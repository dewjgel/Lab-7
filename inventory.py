from product import Product

class Inventory:
    def __init__(self):
        self.products = []

    def add_product(self, product):
        if not isinstance(product, Product):
            raise TypeError("Only Product objects can be added to the inventory.")

        if self.search_product(product.product_id) is not None:
            raise ValueError("Product ID already exists in the inventory.")
            return False

        self.products.append(product)
        print("Product added successfully.")
        return True
     
    def search_product(self, product_id):
        for product in self.products:
            if product.product_id.lower() == product_id.lower():
                return product
            
        return None

    def display_inventory(self):
        print("Current Inventory")
        print("-----------------------------------------------")

        if len(self.products) == 0:
            print("Inventory is empty.")
        else:
             for product in self.products:
                product.display_information()
                print("Fufillment:", product.get_fufillment_method())

        print("-----------------------------------------------")

    def get_products(self):
        return self.products.copy()
