from schemas.product_manager import Product, Category
from utils.os_utils import get_main_dir, save_pickle_file


def read_inventory():
    """
    Lee el archivo de inventario y crea un diccionario de categorías con sus respectivos productos.
    """
    categories = {}

    with open(get_main_dir("db/inventory.txt"), "r") as file:
        for line in file:
            parts = line.strip().split(" ")
            (
                category_id,
                category_name,
                product_id,
                product_name,
                product_price,
                product_quantity,
                product_weight,
            ) = parts

            category_id = int(category_id)
            product_id = int(product_id)
            product_price = float(product_price)
            product_quantity = int(product_quantity)
            product_weight = float(product_weight)

            if category_id not in categories:
                categories[category_id] = Category(category_id, category_name)

            product = Product(
                product_id,
                product_name,
                product_price,
                product_quantity,
                product_weight,
            )
            categories[category_id].products.append(product)

    return categories


def db_main():
    """
    Lee el inventario desde un archivo de texto, lo guarda en un archivo pickle y notifica al usuario.
    """
    categories = read_inventory()
    save_pickle_file(categories, "inventory.pickle")
    print("\n\n[+] Inventory data has been saved as inventory.pickle")
