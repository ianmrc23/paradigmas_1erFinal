import os
import pickle
from schemas.product_manager import Product, Category

def get_main_dir(subdir=""):
    """
    Obtiene el directorio principal del proyecto.
    """
    current_dir = os.path.dirname(os.path.abspath(__file__))
    main_dir = os.path.join(current_dir, "..")
    if subdir:
        return os.path.join(main_dir, subdir)
    return main_dir


def save_pickle_file(data, filename):
    """
    Guarda datos en un archivo pickle.
    """
    filepath = get_main_dir(f"db/{filename}")
    with open(filepath, "wb") as file:
        pickle.dump(data, file)


def load_pickle_file(filename):
    """
    Carga datos desde un archivo pickle.
    """
    filepath = get_main_dir(f"db/{filename}")
    with open(filepath, "rb") as file:
        return pickle.load(file)


def file_exists(file_path):
    """
    Verifica si un archivo existe en la ruta especificada.
    """
    return os.path.exists(get_main_dir(f"db/{file_path}"))


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
