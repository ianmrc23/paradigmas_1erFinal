from utils.os_utils import save_pickle_file
from schemas.polymorphism import CardPayment, CashPayment, ExpressShipping, InStorePickup, QRPayment, StandardShipping, calculate_shipping, process_payment

from tkinter import messagebox
import tkinter as tk


class CheckoutPage(tk.Frame):
    def __init__(self, parent, controller):
        super().__init__(parent)
        self.controller = controller

        self.label = tk.Label(self, text="CHECKOUT", font=("Arial", 18))
        self.label.pack(pady=10)

        self.selected_payment = tk.StringVar()
        self.selected_shipping = tk.StringVar()

        # Frame para métodos de pago
        frame_payment = tk.LabelFrame(self, text="Payment Methods")
        frame_payment.pack(pady=10)

        payment_methods = [
            ("Cash Payment", "cash"),
            ("Card Payment", "card"),
            ("QR Payment", "qr")
        ]

        for text, value in payment_methods:
            radiobutton = tk.Radiobutton(frame_payment, text=text, variable=self.selected_payment,
                                         value=value, anchor="w")
            radiobutton.pack(fill="both", padx=10, pady=5)

        # Frame para métodos de envío
        frame_shipping = tk.LabelFrame(self, text="Shipping Methods")
        frame_shipping.pack(pady=10)

        shipping_methods = [
            ("Standard Shipping", "standard"),
            ("Express Shipping", "express"),
            ("In-Store Pickup", "pickup")
        ]

        for text, value in shipping_methods:
            radiobutton = tk.Radiobutton(frame_shipping, text=text, variable=self.selected_shipping,
                                         value=value, anchor="w")
            radiobutton.pack(fill="both", padx=10, pady=5)

        self.message_label = tk.Label(self, text="", fg="red")
        self.message_label.pack(pady=5)

        # Botón para proceder al checkout
        btn_checkout = tk.Button(
            self, text="Pay", command=self.process_checkout)
        btn_checkout.pack(pady=10)

        # Botón para volver al main menu
        btn_back = tk.Button(
            self, text="Back", command=lambda: controller.show_frame("MainPage"))
        btn_back.pack(pady=10)

    def process_checkout(self):
        if not self.controller.client.cart:
            self.message_label.config(text="Your cart is empty.", fg="red")
            return

        payment_method = self.selected_payment.get()
        shipping_method = self.selected_shipping.get()

        if not payment_method:
            self.message_label.config(
                text="Please select a payment method.", fg="red")
            return

        if not shipping_method:
            self.message_label.config(
                text="Please select a shipping method.", fg="red")
            return

        # Obtener las clases correspondientes a los métodos seleccionados
        payment_class = {
            "cash": CashPayment,
            "card": CardPayment,
            "qr": QRPayment
        }.get(payment_method)

        shipping_class = {
            "standard": StandardShipping,
            "express": ExpressShipping,
            "pickup": InStorePickup
        }.get(shipping_method)

        # Procesar el pago y el envío
        total_amount, total_weight = self.controller.client.calculate_totals()
        payment_instance = payment_class()
        total_with_discount = process_payment(payment_instance, total_amount)

        shipping_instance = shipping_class()
        shipping_cost = calculate_shipping(
            shipping_instance, total_weight, self.controller.client.client_distance_from_store, len(self.controller.client.cart))
        total_amount_with_shipping = total_with_discount + shipping_cost

        # Mostrar resumen del checkout
        summary_message = (
            f"Total Amount: ${total_amount:.2f}\n"
            f"Shipping Cost: ${shipping_cost:.2f}\n"
            f"Total Amount with Shipping: ${total_amount_with_shipping:.2f}\n"
            f"Total Amount Paid: ${total_with_discount:.2f}"
        )

        messagebox.showinfo("Checkout Summary", summary_message)

        # Limpiar el carrito y guardar los cambios
        self.controller.client.cart.clear()
        save_pickle_file(self.controller.client, f"{self.controller.client.client_email}.pickle")

        # Mostrar un mensaje de confirmación en la interfaz
        self.message_label.config(
            text="Checkout completed successfully.", fg="green")
