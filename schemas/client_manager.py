from typing import List
from schemas.file_manager import FileManager


class Client:
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
        self.file_manager = FileManager()

    def calculate_totals(self):
        total_price: float = 0.0
        total_weight: float = 0.0

        for item in self.cart:
            product = item["product"]
            quantity = item["quantity"]

            total_price += product.product_price * quantity
            total_weight += product.product_weight * quantity

        return total_price, total_weight

    def add_to_cart(self, product, quantity):
        for item in self.cart:
            if item["product"].product_id == product.product_id:
                item["quantity"] += quantity
                break
        else:
            cart_item = {"product": product, "quantity": quantity}
            self.cart.append(cart_item)

        self.file_manager.save_pickle_file(self, f"{self.client_email}.pickle")
