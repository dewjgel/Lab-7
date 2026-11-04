import json
from product import Product
from inventory import Inventory

FILE_NAME = "inventory.json" 

DEFAULT_INVENTORY = [
    {
        "id": "P001",
        "name": "Laptop",
        "price": 1200.00,
        "stock": 15
    },
    {
        "id": "P002",
        "name": "Mouse",
        "price": 25.50,
        "stock": 40
    },
    {
        "id": "P003",
        "name": "Keyboard",
        "price": 45.00,
        "stock": 25
    }
]

def load_inventory():

    try: 
       with open(FILE_NAME, "r") as file:
        data = json.load(file)
        inventory = Inventory()

        for item in data:
            product = Product(
                item["id"],
                item["name"],
                item["price"],
                item["stock"]
            )

            if not inventory.add_product(product):
                raise ValueError("Duplicate product ID in inventory")
        
        print("Inventory loaded successfully.")
        return inventory
       

    except FileNotFoundError:

        print("inventory.json not found")
        print("Starting with an empty inventory")
        return create_default_inventory()
    
    except (json.JSONDecodeError, ValueError, TypeError, KeyError) as error:
        print("Error loading inventory:", error)
        print("Starting with an empty inventory.")
        return create_default_inventory()

def create_default_inventory():
    inventory = Inventory()

    for item in DEFAULT_INVENTORY:
        product = Product(
            item["id"],
            item["name"],
            item["price"],
            item["stock"]
        )
        inventory.add_product(product)

    return inventory

def save_inventory(inventory):
    data = []

    for product in inventory.get_products():
        data.append({
            "id": product.product_id,
            "name": product.name,
            "price": product.price,
            "stock": product.stock
        })

    try:
        with open(FILE_NAME, "w") as file:
            json.dump(data, file, indent=4)

        print("Inventory saved successfully to inventory.json.")

    except OSError as error:
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

    product = Product(product_id, name, price, stock)

    inventory.add_product(product)

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

            if new_stock < 0:
                print("Stock cannot be negative.")
            else:
                product.update_stock(new_stock)
                print("Stock updated successfully.")
                return

        except ValueError:
            print("Please enter a valid whole number.")

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
        print("--------------------------------------------")


def main():
    print("=====================================")
    print("INVENTORY MANAGEMENT SYSTEM")
    print("=====================================")

    inventory = load_inventory()

    try:
        with open(FILE_NAME, "r") as file:
            json.load(file)

    except (FileNotFoundError, json.JSONDecodeError):
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