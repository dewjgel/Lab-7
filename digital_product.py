from product import Product

class DigitalProduct(Product):
    def __init__(self, product_id, name, price, stock, download_size):
        super().__init__(product_id, name, price, stock)
        self.download_size = float(download_size)
        if self.download_size < 0:
            raise ValueError("Download size cannot be negative.")

    def display_information(self):
        super().display_information()
        print(f"Download Size: {self.download_size:.2f} MB")

    def get_fufillment_method(self):
        return "This product is delivered digitally."