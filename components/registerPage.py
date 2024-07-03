from utils.os_utils import save_pickle_file
from schemas.client_manager import Client

import tkinter as tk


class RegisterPage(tk.Frame):
    def __init__(self, parent, controller):
        super().__init__(parent)
        self.controller = controller

        label = tk.Label(self, text="Register", font=("Arial", 18))
        label.pack(pady=10)

        tk.Label(self, text="ID: ").pack()
        self.entry_id = tk.Entry(self)
        self.entry_id.pack()

        tk.Label(self, text="Name: ").pack()
        self.entry_name = tk.Entry(self)
        self.entry_name.pack()

        tk.Label(self, text="Email: ").pack()
        self.entry_email = tk.Entry(self)
        self.entry_email.pack()

        tk.Label(self, text="Password: ").pack()
        self.entry_password = tk.Entry(self, show='*')
        self.entry_password.pack()

        tk.Label(self, text="Address: ").pack()
        self.entry_address = tk.Entry(self)
        self.entry_address.pack()

        tk.Label(self, text="Distance from store: ").pack()
        self.entry_distance = tk.Entry(self)
        self.entry_distance.pack()

        self.lbl_message = tk.Label(self, text="", fg="red")
        self.lbl_message.pack(pady=5)

        register_button = tk.Button(self, text="Register",
                                    command=self.register_user)
        register_button.pack(pady=10)

        back_button = tk.Button(self, text="Back",
                                command=lambda: controller.show_frame("StartPage"))
        back_button.pack(pady=10)

    def register_user(self):
        try:
            client_id = int(self.entry_id.get())
            client_name = self.entry_name.get()
            client_email = self.entry_email.get()
            client_password = self.entry_password.get()
            client_address = self.entry_address.get()
            client_distance = float(self.entry_distance.get())

            if client_id <= 0:
                raise ValueError("ID must be a positive integer.")

            if client_distance < 0:
                raise ValueError("Distance must be a non-negative number.")

            new_client = Client(
                client_id=client_id,
                client_name=client_name,
                client_email=client_email,
                client_password=client_password,
                client_address=client_address,
                client_distance=client_distance
            )

            save_pickle_file(new_client, f"{client_email}.pickle")

            self.controller.show_frame("StartPage")

        except ValueError as e:
            self.lbl_message.config(text=f"Error: {e}", fg="red")
