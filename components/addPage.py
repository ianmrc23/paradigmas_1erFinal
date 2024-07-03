from schemas.file_manager import FileManager
import tkinter as tk
from tkinter import messagebox


class AddProductPage(tk.Frame):
    def __init__(self, parent, controller):
        super().__init__(parent)
        self.controller = controller
        self.file_manager = FileManager()
        self.categories = self.file_manager.load_pickle_file("inventory.pickle")

        self.label = tk.Label(
            self, text="ADD PRODUCT TO CART", font=("Arial", 18))
        self.label.pack(pady=10)

        self.show_categories()

        btn_back = tk.Button(
            self, text="Back", command=lambda: controller.show_frame("MainPage"))
        btn_back.pack(pady=10)

    def show_categories(self):
        self.clear_frame()

        label_categories = tk.Label(
            self, text="Select a Category", font=("Arial", 14))
        label_categories.pack(pady=10)

        self.category_buttons = []
        for idx, category in enumerate(self.categories.values(), 1):
            category_button = tk.Button(self, text=f"{idx}. {category.category_name}", command=lambda c=category: self.show_products(c))
            category_button.pack(pady=5)
            self.category_buttons.append(category_button)

    def show_products(self, category):
        self.clear_frame()

        label_category = tk.Label(self, text=f"Category: {category.category_name}", font=("Arial", 14))
        label_category.pack(pady=10)

        self.product_buttons = []
        for idx, product in enumerate(category.products, 1):
            product_button = tk.Button(self, text=f"{idx}. {product.product_name} - Stock: {product.product_quantity} - Price: ${product.product_price}", command=lambda p=product: self.select_product(p))
            product_button.pack(pady=5)
            self.product_buttons.append(product_button)

        btn_back = tk.Button(self, text="Back", command=self.show_categories)
        btn_back.pack(pady=10)

        btn_back_main_menu = tk.Button(
            self, text="Main Menu", command=lambda: self.controller.show_frame("MainPage"))
        btn_back_main_menu.pack(pady=10)

    def select_product(self, product):
        self.clear_frame()

        label_product = tk.Label(self, text=f"Product: {product.product_name}", font=("Arial", 14))
        label_product.pack(pady=10)

        label_details = tk.Label(self, text=f"Stock: {product.product_quantity} - Price: ${product.product_price}")
        label_details.pack(pady=5)

        label_quantity = tk.Label(self, text="Enter quantity:")
        label_quantity.pack(pady=5)
        self.quantity_entry = tk.Entry(self)
        self.quantity_entry.pack(pady=5)

        btn_add_to_cart = tk.Button(
            self, text="Add to Cart", command=lambda: self.add_to_cart(product))
        btn_add_to_cart.pack(pady=10)

        btn_back = tk.Button(
            self, text="Back", command=lambda: self.show_products(self.current_category))
        btn_back.pack(pady=10)

        btn_back_main_menu = tk.Button(
            self, text="Main Menu", command=lambda: self.controller.show_frame("MainPage"))
        btn_back_main_menu.pack(pady=10)

        self.current_category = next(
            category for category in self.categories.values() if product in category.products)

    def add_to_cart(self, product):
        try:
            quantity = int(self.quantity_entry.get())
            if 0 < quantity <= product.product_quantity:
                product.product_quantity -= quantity

                self.controller.client.add_to_cart(product, quantity)

                self.file_manager.save_pickle_file(self.controller.client, f"{self.controller.client.client_email}.pickle")
                self.file_manager.save_pickle_file(
                    self.categories, "inventory.pickle")

                self.show_products(self.current_category)

                messagebox.showinfo(
                    title=None, message="Product added to cart successfully.")
            else:
                messagebox.showerror(title=None, message="Invalid quantity.")
        except ValueError:
            messagebox.showerror(
                title=None, message="Please enter a valid number.")

    def clear_frame(self):
        for widget in self.winfo_children():
            widget.pack_forget()
