import tkinter as tk


class ProfilePage(tk.Frame):
    def __init__(self, parent, controller):
        super().__init__(parent)
        self.controller = controller

        self.label = tk.Label(self, text="PROFILE", font=("Arial", 18))
        self.label.pack(pady=10)

        self.id_label = tk.Label(self, text="")
        self.id_label.pack(pady=5)

        self.name_label = tk.Label(self, text="")
        self.name_label.pack(pady=5)

        self.email_label = tk.Label(self, text="")
        self.email_label.pack(pady=5)

        self.address_label = tk.Label(self, text="")
        self.address_label.pack(pady=5)

        self.distance_label = tk.Label(self, text="")
        self.distance_label.pack(pady=5)

        self.password_label = tk.Label(self, text="")
        self.password_label.pack(pady=5)

        btn_close = tk.Button(self, text="Back", command=lambda: controller.show_frame("MainPage"))
        btn_close.pack(pady=10)

    def update_profile(self):
        client = self.controller.client
        
        self.id_label.config(text=f"ID: {client.client_id}")
        self.name_label.config(text=f"Name: {client.client_name}")
        self.email_label.config(text=f"Email: {client.client_email}")
        self.address_label.config(text=f"Address: {client.client_address}")
        self.distance_label.config(text=f"Distance: {client.client_distance_from_store} km")
        self.password_label.config(text=f"Password: {client.client_password}")
