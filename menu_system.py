import json

from product import Product
from physical_product import PhysicalProduct
from digital_product import DigitalProduct
from can_be_shipped import CanBeShipped
from inventory import Inventory

FILE_NAME = "inventory.json" 

DEFAULT_INVENTORY = [
    {
        type: "PhysicalProduct",
        "id": "P001",
        "name": "Laptop",
        "price": 1200.00,
        "stock": 15,
        "weight": 2.5
    },
    {
        type: "PhysicalProduct",
        "id": "P002",
        "name": "Mouse",
        "price": 25.50,
        "stock": 40,
        "weight": 0.2
    },
    {
        "type": "DigitalProduct",
        "id": "P003",
        "name": "Antivirus Software",
        "price": 45.00,
        "stock": 25,
        "download_size": 500
    }
]
def create_product(item):

    product_type = item["type"].lower

    if product_type == "physicalproduct":
        return PhysicalProduct(
            item["id"],
            item["name"],
            item["price"],
            item["stock"],
            item["weight"]
        )
    elif product_type == "digitalproduct":
        return DigitalProduct(
            item["id"],
            item["name"],
            item["price"],
            item["stock"],
            item["download_size"]
        )
    else:
        raise ValueError(f"Unknown product type: {item['type']}")

def load_inventory():

    try: 
       with open(FILE_NAME, "r") as file:
        data = json.load(file)

        if not isinstance(data, list):
            raise ValueError("Inventory data should be a list of products.")

        inventory = Inventory()

        for item in data:
            product = create_product(item)
            inventory.add_product(product)
 
        print("Inventory loaded successfully.")
        return inventory
       

    except FileNotFoundError:

        print("inventory.json not found")
        print("Creating default inventory.")
        return create_default_inventory()
    
    except (json.JSONDecodeError, ValueError, TypeError, KeyError, OverflowError) as error:
        print("Error loading inventory:", error)
        print("Creating default inventory.")
        return create_default_inventory()

def create_default_inventory():
    inventory = Inventory()

    for item in DEFAULT_INVENTORY:
        product = create_product(item)
        inventory.add_product(product)

    return inventory

def save_inventory(inventory):
    data = []

    for product in inventory.get_products():
        if isinstance(product, PhysicalProduct):
            item = {
                "type": "PhysicalProduct",
                "id": product.product_id,
                "name": product.name,
                "price": product.price,
                "stock": product.stock,
                "weight": product.weight
            }

        elif isinstance(product, DigitalProduct):
            item = {
                "type": "DigitalProduct",
                "id": product.product_id,
                "name": product.name,
                "price": product.price,
                "stock": product.stock,
                "download_size": product.download_size
        }
        else:

            raise TypeError("Unsupported product type.")

        data.append(item)

    try:
        with open(FILE_NAME, "w") as file:
            json.dump(data, file, indent=4)

        print("Inventory saved successfully to inventory.json.")

    except (OSError, TypeError, ValueError) as error:
        print("Error saving inventory:", error)

def display_menu():
    print("\n ---------- MENU ----------")
    print("1. Display All Products")
    print("2. Add New Product")
    print("3. Update Product Stock")
    print("4. Search Product by ID")
    print("5. Save Inventory")
    print("6. Exit")
    print("---------------------------")

def add_product(inventory):
    print("\nAdd New Product")
    
    product_id = input("Enter Product ID: ").strip()

    if not product_id:
        print("Product ID cannot be empty.")
        return

    if inventory.search_product(product_id) is not None:
        print("Product ID already exists.")
        return

    name = input("Enter Product Name: ").strip()

    if not name:
        print("Product Name cannot be empty.")
        return

    while True:
        try:
            price = float(input("Price: "))

            if price < 0:
                print("Price cannot be negative.")
            else:
                break

        except ValueError:
            print("Please enter a valid price.")

    while True:
        try:
            stock = int(input("Stock Quantity: "))

            if stock < 0:
                print("Stock cannot be negative.")
            else:
                break

        except ValueError:
            print("Please enter a whole number.")

    print("\nSelect Product Type:")
    print("1. Physical Product")
    print("2. Digital Product")

    product_type = input("Enter option: ").strip()

    try:
        if product_type == "1":
            weight = float(input("Weight (kg): "))

            if weight < 0:
                print("Weight cannot be negative.")
                return
            product = PhysicalProduct(product_id, name, price, stock, weight)

        elif product_type == "2":
            download_size = float(input("Enter Download Size (MB): "))

            if download_size < 0:
                print("Download size cannot be negative.")
                return

            product = DigitalProduct(product_id, name, price, stock, download_size)

        else: 
            print("Invalid product type.")
            return

        inventory.add_product(product)

        print("Fulfilment:", product.get_fulfilment_info())
        if isinstance(product, CanBeShipped):
                print(f"Shipping Cost: ${product.calculate_shipping_cost():.2f}")
                

    except (ValueError, OverflowError) as error:
        print("Invalid product information:", error)

def update_product_stock(inventory):
    print("\nUpdate Stock")

    product_id = input("Enter Product ID: ").strip()
    product = inventory.search_product(product_id)

    if product is None:
        print("Product not found.")
        return

    print("Product Found:")
    print("Name:", product.name)
    print("Current Stock:", product.stock)

    while True:
        try:
            new_stock = int(input("New Stock Quantity: "))

            product.update_stock(new_stock)
            print("Stock updated successfully.")
            return

        except ValueError as error:
            print("Invalid stock quantity:", error)

def search_product(inventory):
    print("\nSearch Product")

    product_id = input("Enter Product ID: ").strip()
    product = inventory.search_product(product_id)

    if product is None:
        print("Product not found.")
    else:
        print("Product Found")
        print("--------------------------------------------")
        product.display_information()
        print("Fulfilment:", product.get_fulfilment_info())
        if isinstance(product, CanBeShipped):
            print(f"Shipping Cost: ${product.calculate_shipping_cost():.2f}")

        print("--------------------------------------------")


def main():
    print("=====================================")
    print("INVENTORY MANAGEMENT SYSTEM")
    print("=====================================")

    inventory = load_inventory()

    try:
        with open(FILE_NAME, "r"):
            pass

    except (FileNotFoundError)
        save_inventory(inventory)

    while True:
        display_menu()
        option = input("Enter option: ").strip()

        if option == "1":
            inventory.display_inventory()

        elif option == "2":
            add_product(inventory)

        elif option == "3":
            update_product_stock(inventory)

        elif option == "4":
            search_product(inventory)

        elif option == "5":
            save_inventory(inventory)

        elif option == "6":
            print("Saving inventory before exit...")
            save_inventory(inventory)
            print("Thank you for using Inventory Management System.")
            print("Program terminated.")
            break

        else:
            print("Invalid option. Please enter 1-6.")

if __name__ == "__main__":
    main()