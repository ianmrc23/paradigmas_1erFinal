import os
import pickle
from schemas.product_manager import Product, Category


class FileManager:
    def __init__(self):
        self.db_dir = os.path.join(os.path.dirname(
            os.path.abspath(__file__)), "..", "db")

    def save_pickle_file(self, data, filename):
        """
        Guarda datos en un archivo pickle.
        """
        filepath = os.path.join(self.db_dir, filename)
        with open(filepath, "wb") as file:
            pickle.dump(data, file)

    def load_pickle_file(self, filename):
        """
        Carga datos desde un archivo pickle.
        """
        filepath = os.path.join(self.db_dir, filename)
        with open(filepath, "rb") as file:
            return pickle.load(file)

    def file_exists(self, filename):
        """
        Verifica si un archivo existe en la ruta especificada.
        """
        filepath = os.path.join(self.db_dir, filename)
        return os.path.exists(filepath)

    def read_inventory(self, filename):
        """
        Lee el archivo de inventario y crea un diccionario de categorías con sus respectivos productos.
        """
        categories = {}

        with open(os.path.join(self.db_dir, filename), "r") as file:
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
                    categories[category_id] = Category(
                        category_id, category_name)

                product = Product(
                    product_id,
                    product_name,
                    product_price,
                    product_quantity,
                    product_weight,
                )
                categories[category_id].products.append(product)

        return categories
