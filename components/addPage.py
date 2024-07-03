
from utils.os_utils import CustomMessageBox, save_pickle_file, load_pickle_file

import tkinter as tk

class AddProductPage(tk.Frame):
    def __init__(self, parent, controller):
        super().__init__(parent)
        self.controller = controller
        self.categories = load_pickle_file("inventory.pickle")

        self.label = tk.Label(self, text="ADD PRODUCT TO CART", font=("Arial", 18))
        self.label.pack(pady=10)

        self.show_categories()

        # Botón para retroceder al main menu
        btn_back = tk.Button(self, text="Back", command=lambda: controller.show_frame("MainPage"))
        btn_back.pack(pady=10)

    def show_categories(self):
        # Limpiar la pantalla antes de mostrar categorías
        self.clear_frame()

        # Mostrar el título de las categorías
        label_categories = tk.Label(self, text="Select a Category", font=("Arial", 14))
        label_categories.pack(pady=10)

        # Mostrar categorías como botones con nombres
        self.category_buttons = []
        for idx, category in enumerate(self.categories.values(), 1):
            category_button = tk.Button(self, text=f"{idx}. {category.category_name}",
                                        command=lambda c=category: self.show_products(c))
            category_button.pack(pady=5)
            self.category_buttons.append(category_button)

        # Botón para retroceder al main menu
        btn_back_main_menu = tk.Button(self, text="Back", command=lambda: self.controller.show_frame("MainPage"))
        btn_back_main_menu.pack(pady=10)
        
    def show_products(self, category):
        # Limpiar la pantalla antes de mostrar productos
        self.clear_frame()

        # Mostrar el título de la categoría seleccionada
        label_category = tk.Label(self, text=f"Category: {category.category_name}", font=("Arial", 14))
        label_category.pack(pady=10)

        # Mostrar productos de la categoría seleccionada
        self.product_buttons = []
        for idx, product in enumerate(category.products, 1):
            product_button = tk.Button(self, text=f"{idx}. {product.product_name} - Stock: {product.product_quantity} - Price: ${product.product_price}",
                                       command=lambda p=product: self.select_product(p))
            product_button.pack(pady=5)
            self.product_buttons.append(product_button)

        # Botón para retroceder a las categorías
        btn_back = tk.Button(self, text="Back", command=self.show_categories)
        btn_back.pack(pady=10)
        
        # Botón para retroceder al main menu
        btn_back_main_menu = tk.Button(self, text="Main Menu", command=lambda: self.controller.show_frame("MainPage"))
        btn_back_main_menu.pack(pady=10)

    def select_product(self, product):
        # Limpiar la pantalla antes de mostrar los detalles del producto
        self.clear_frame()

        # Mostrar el nombre del producto
        label_product = tk.Label(self, text=f"Product: {product.product_name}", font=("Arial", 14))
        label_product.pack(pady=10)

        # Mostrar detalles del producto
        label_details = tk.Label(self, text=f"Stock: {product.product_quantity} - Price: ${product.product_price}")
        label_details.pack(pady=5)

        # Campo de entrada para la cantidad
        label_quantity = tk.Label(self, text="Enter quantity:")
        label_quantity.pack(pady=5)
        self.quantity_entry = tk.Entry(self)
        self.quantity_entry.pack(pady=5)

        # Botón para añadir al carrito
        btn_add_to_cart = tk.Button(self, text="Add to Cart", command=lambda: self.add_to_cart(product))
        btn_add_to_cart.pack(pady=10)

        # Botón para retroceder a los productos
        btn_back = tk.Button(self, text="Back", command=lambda: self.show_products(self.current_category))
        btn_back.pack(pady=10)
        
        # Botón para retroceder al main menu
        btn_back_main_menu = tk.Button(self, text="Main Menu", command=lambda: self.controller.show_frame("MainPage"))
        btn_back_main_menu.pack(pady=10)

        # Guardar la categoría actual para regresar
        self.current_category = next(category for category in self.categories.values() if product in category.products)

    def add_to_cart(self, product):
        try:
            quantity = int(self.quantity_entry.get())
            if 0 < quantity <= product.product_quantity:
                product.product_quantity -= quantity
                self.controller.client.add_to_cart(product, quantity)
                save_pickle_file(self.controller.client, f"{self.controller.client.client_email}.pickle")
                save_pickle_file(self.categories, "inventory.pickle")
                self.show_products(self.current_category)
                custom_message = CustomMessageBox(self, "Success", "Product added to cart successfully.", bg_color="white", text_color="green")
                custom_message.show()
            else:
                custom_message = CustomMessageBox(self, "Error", "Invalid quantity.", bg_color="white", text_color="red")
                custom_message.show()
        except ValueError:
            custom_message = CustomMessageBox(self, "Error", "Please enter a valid number.", bg_color="white", text_color="red")
            custom_message.show()

    def clear_frame(self):
        # Limpiar todos los widgets en el frame
        for widget in self.winfo_children():
            widget.pack_forget()
 