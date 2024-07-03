from utils.os_utils import save_pickle_file, load_pickle_file

from tkinter import messagebox
import tkinter as tk


class CartPage(tk.Frame):
    def __init__(self, parent, controller):
        super().__init__(parent)
        self.controller = controller

        self.label = tk.Label(self, text="MY CART", font=("Arial", 18))
        self.label.pack(pady=10)

        self.cart_listbox = tk.Listbox(self, width=50, height=10)
        self.cart_listbox.pack(pady=10)

        # Botón para ver el carrito
        btn_view_cart = tk.Button(self, text="View Cart", command=self.view_cart)
        btn_view_cart.pack(pady=5)

        # Botón para remover un producto del carrito
        btn_remove_product = tk.Button(self, text="Remove Product", command=self.remove_product)
        btn_remove_product.pack(pady=5)

        # Botón para limpiar el carrito
        btn_clear_cart = tk.Button(self, text="Clear Cart", command=self.clear_cart)
        btn_clear_cart.pack(pady=5)

        # Botón para volver al main menu
        btn_back = tk.Button(self, text="Back", command=lambda: controller.show_frame("MainPage"))
        btn_back.pack(pady=10)

    def view_cart(self):
        self.cart_listbox.delete(0, tk.END)
        cart_items = self.controller.client.cart
        if not cart_items:
            messagebox.showinfo("Cart", "Your cart is empty.")
        else:
            for item in cart_items:
                product = item["product"]
                quantity = item["quantity"]
                self.cart_listbox.insert(tk.END, f"{product.product_name} - Quantity: {quantity}")

    def remove_product(self):
        selected_index = self.cart_listbox.curselection()
        if not selected_index:
            messagebox.showwarning("Remove Product", "Please select a product to remove.")
            return

        product_index = selected_index[0]
        selected_item = self.controller.client.cart[product_index]
        product = selected_item["product"]
        quantity_to_remove = selected_item["quantity"]

        confirm = messagebox.askyesno("Remove Product", f"Are you sure you want to remove {quantity_to_remove} {product.product_name}(s)?")
        if not confirm:
            return

        self.controller.client.cart.pop(product_index)

        # Devolver el producto al inventario
        categories = load_pickle_file("inventory.pickle")
        for category in categories.values():
            for prod in category.products:
                if prod.product_id == product.product_id:
                    prod.product_quantity += quantity_to_remove
                    break

        save_pickle_file(categories, "inventory.pickle")
        save_pickle_file(self.controller.client, f"{self.controller.client.client_email}.pickle")

        self.controller.reset_page("AddProductPage")
        
        self.view_cart()
        messagebox.showinfo("Remove Product", f"{quantity_to_remove} {product.product_name}(s) have been removed from your cart.")

    def clear_cart(self):
        if not self.controller.client.cart:
            messagebox.showinfo("Clear Cart", "Your cart is already empty.")
            return

        confirm = messagebox.askyesno("Clear Cart", "Are you sure you want to clear your cart?")
        if not confirm:
            return

        categories = load_pickle_file("inventory.pickle")
        for item in self.controller.client.cart:
            product = item["product"]
            quantity_to_add_back = item["quantity"]
            for category in categories.values():
                for prod in category.products:
                    if prod.product_id == product.product_id:
                        prod.product_quantity += quantity_to_add_back
                        break

        save_pickle_file(categories, "inventory.pickle")

        self.controller.client.cart.clear()
        save_pickle_file(self.controller.client, f"{self.controller.client.client_email}.pickle")

        self.controller.reset_page("AddProductPage")

        self.view_cart()
        messagebox.showinfo("Clear Cart", "Your cart has been successfully cleared.")
        
