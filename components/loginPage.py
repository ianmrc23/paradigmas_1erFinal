from tkinter import messagebox
from utils.utils import file_exists, load_pickle_file

import tkinter as tk


class LoginPage(tk.Frame):
    def __init__(self, parent, controller):
        super().__init__(parent)
        self.controller = controller

        label = tk.Label(self, text="LOGIN", font=("Arial", 18))
        label.pack(pady=10)

        tk.Label(self, text="Email:").pack()
        self.entry_email = tk.Entry(self)
        self.entry_email.pack(pady=5)

        tk.Label(self, text="Password:").pack()
        self.entry_password = tk.Entry(self, show="*")
        self.entry_password.pack(pady=5)

        login_button = tk.Button(self, text="Login", command=self.login_user)
        login_button.pack(pady=10)

        back_button = tk.Button(self, text="Back", command=lambda: controller.show_frame("StartPage"))
        back_button.pack(pady=10)

    def login_user(self):
        client_email = self.entry_email.get()
        client_password = self.entry_password.get()
        client_file = f"{client_email}.pickle"

        if file_exists(client_file):
            client = load_pickle_file(client_file)

            if client.client_password == client_password:
                self.controller.client = client
                self.controller.show_frame("MainPage")
            else:
                messagebox.showerror(title=None, message="Incorrect password.")
        else:
            messagebox.showerror(title=None, message="No account found with this email.")
