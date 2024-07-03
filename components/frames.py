from components.addPage import AddProductPage
from components.cartPage import CartPage
from components.checkPage import CheckoutPage
from components.loginPage import LoginPage
from components.profilePage import ProfilePage
from components.registerPage import RegisterPage

import tkinter as tk


class StoreApp(tk.Tk):
    def __init__(self):
        super().__init__()
        self.title("Store")

        self.container = tk.Frame(self)
        self.container.pack(side="top", expand=True)

        self.frames = {}

        for F in (StartPage, LoginPage, RegisterPage, MainPage, ProfilePage, CheckoutPage, AddProductPage, CartPage):
            page_name = F.__name__
            frame = F(parent=self.container, controller=self)
            self.frames[page_name] = frame

            frame.grid(row=0, column=0, sticky="nsew")

        self.show_frame("StartPage")

    def show_frame(self, page_name):
        frame = self.frames[page_name]
        frame.tkraise()

        if page_name == "StartPage":
            self.geometry("400x220")
        elif page_name == "LoginPage":
            self.geometry("400x300")
        elif page_name == "RegisterPage":
            self.geometry("400x500")
        elif page_name == "MainPage":
            self.geometry("400x330")
        elif page_name == "ProfilePage":
            frame.update_profile()
            self.geometry("400x310")
        elif page_name == "CheckoutPage":
            self.geometry("400x500")
        elif page_name == "AddProductPage":
            self.geometry("400x600")
        elif page_name == "CartPage":
            self.geometry("400x600")

    def reset_page(self, page_name):
        if page_name in self.frames:
            self.frames[page_name].destroy()
            del self.frames[page_name]

        container = self.frames["MainPage"].master
        frame_class = globals()[page_name]
        new_frame = frame_class(parent=container, controller=self)
        self.frames[page_name] = new_frame
        new_frame.grid(row=0, column=0, sticky="nsew")


class StartPage(tk.Frame):
    def __init__(self, parent, controller):
        super().__init__(parent)
        self.controller = controller

        label = tk.Label(self, text="Welcome to the Store", font=("Arial", 18))
        label.pack(pady=10, anchor='center')

        register_button = tk.Button(self, text="Register",
                                    command=lambda: controller.show_frame("RegisterPage"))
        register_button.pack(pady=10, anchor='center')

        login_button = tk.Button(self, text="Login",
                                 command=lambda: controller.show_frame("LoginPage"))
        login_button.pack(pady=10, anchor='center')

        close_button = tk.Button(self, text="Close",
                                 command=controller.quit)
        close_button.pack(pady=10, anchor='center')


class MainPage(tk.Frame):
    def __init__(self, parent, controller):
        super().__init__(parent)
        self.controller = controller

        label = tk.Label(self, text="MAIN MENU", font=("Arial", 18))
        label.pack(pady=10)

        btn_add_product = tk.Button(
            self, text="Add Product", command=self.open_add_product)
        btn_add_product.pack(pady=10)

        btn_my_cart = tk.Button(self, text="My Cart",
                                command=self.open_my_cart)
        btn_my_cart.pack(pady=10)

        btn_checkout = tk.Button(
            self, text="Checkout", command=self.open_checkout)
        btn_checkout.pack(pady=10)

        btn_profile = tk.Button(self, text="Profile",
                                command=self.open_profile)
        btn_profile.pack(pady=10)

        btn_logout = tk.Button(self, text="Logout", command=self.logout)
        btn_logout.pack(pady=10)

    def open_add_product(self):
        self.controller.show_frame("AddProductPage")

    def open_my_cart(self):
        self.controller.show_frame("CartPage")

    def open_checkout(self):
        self.controller.show_frame("CheckoutPage")

    def open_profile(self):
        self.controller.show_frame("ProfilePage")

    def logout(self):
        self.controller.show_frame("StartPage")
