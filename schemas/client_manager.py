from typing import List

from utils.os_utils import save_pickle_file


class Client:
    """
    Representa un cliente de la tienda.

    Attributes:
        client_id (int): El ID del cliente.
        client_name (str): El nombre del cliente.
        client_email (str): El email del cliente.
        client_password (str): La contraseña del cliente.
        client_address (str): La dirección del cliente.
        client_distance_from_store (float): La distancia del cliente a la tienda.
        cart (List[dict]): El carrito de compras del cliente.
    """

    def __init__(
        self,
        client_id: int,
        client_name: str,
        client_email: str,
        client_password: str,
        client_address: str,
        client_distance: float,
    ):
        self.client_id = client_id
        self.client_name = client_name
        self.client_email = client_email
        self.client_password = client_password
        self.client_address = client_address
        self.client_distance_from_store = client_distance
        self.cart: List[dict] = []

    def calculate_totals(self):
        """
        Calcula el precio total y el peso total de los productos en el carrito.
        """
        total_price: float = 0.0
        total_weight: float = 0.0

        for item in self.cart:
            product = item["product"]
            quantity = item["quantity"]

            total_price += product.product_price * quantity
            total_weight += product.product_weight * quantity

        return total_price, total_weight

    def add_to_cart(self, product, quantity):
        """
        Agrega un producto al carrito del cliente.
        """
        for item in self.cart:
            if item["product"].product_id == product.product_id:
                item["quantity"] += quantity
                break
        else:
            cart_item = {"product": product, "quantity": quantity}
            self.cart.append(cart_item)

        save_pickle_file(self, f"{self.client_email}.pickle")
