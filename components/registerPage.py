from schemas.file_manager import FileManager
from schemas.client_manager import Client
from tkinter import messagebox
import tkinter as tk


class RegisterPage(tk.Frame):
    def __init__(self, parent, controller):
        super().__init__(parent)
        self.file_manager = FileManager()
        self.controller = controller

        label = tk.Label(self, text="REGISTER", font=("Arial", 18))
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

        register_button = tk.Button(
            self, text="Register", command=self.register_user)
        register_button.pack(pady=10)

        back_button = tk.Button(
            self, text="Back", command=lambda: controller.show_frame("StartPage"))
        back_button.pack(pady=10)

    def register_user(self):
        client_id = self.entry_id.get()
        client_name = self.entry_name.get()
        client_email = self.entry_email.get()
        client_password = self.entry_password.get()
        client_address = self.entry_address.get()
        client_distance = self.entry_distance.get()

        if not (client_id and client_name and client_email and client_password and client_address and client_distance):
            messagebox.showerror(
                title=None, message="Please fill in all fields.")
            return

        if self.file_manager.file_exists(f"{client_email}.pickle"):
            messagebox.showerror(
                title=None, message="Email is already registered.")
            return

        try:
            client_id = int(client_id)
            client_distance = float(client_distance)

            if client_id <= 0:
                messagebox.showerror(
                    title=None, message="ID must be a positive integer.")
                return

            if client_distance < 0:
                messagebox.showerror(
                    title=None, message="Distance must be a non-negative number.")
                return

            new_client = Client(
                client_id=client_id,
                client_name=client_name,
                client_email=client_email,
                client_password=client_password,
                client_address=client_address,
                client_distance=client_distance
            )

            self.file_manager.save_pickle_file(
                new_client, f"{client_email}.pickle")

            self.controller.show_frame("StartPage")

        except ValueError as e:
            messagebox.showerror(title=None, message=f"Error: {e}")
