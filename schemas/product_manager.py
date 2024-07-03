from typing import List


class Product:
    """
    Representa un producto en la tienda.

    Attributes:
        product_id (int): El ID único del producto.
        product_name (str): El nombre del producto.
        product_price (float): El precio del producto.
        product_quantity (int): La cantidad disponible del producto.
        product_weight (float): El peso del producto.
    """

    def __init__(
        self,
        product_id: int,
        product_name: str,
        product_price: float,
        product_quantity: int,
        product_weight: float
    ):
        self.product_id = product_id
        self.product_name = product_name
        self.product_price = product_price
        self.product_quantity = product_quantity
        self.product_weight = product_weight


class Category:
    """
    Representa una categoría de productos en la tienda.

    Attributes:
        category_id (int): El ID único de la categoría.
        category_name (str): El nombre de la categoría.
        products (List[Product]): La lista de productos en esta categoría.
    """

    def __init__(
        self,
        category_id: int,
        category_name: str
    ):
        self.category_id = category_id
        self.category_name = category_name
        self.products: List[Product] = []
