from utils.utils import save_pickle_file
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

        self.payment_methods = {
            "cash": ("Cash Payment", CashPayment),
            "card": ("Card Payment", CardPayment),
            "qr": ("QR Payment", QRPayment)
        }

        self.shipping_methods = {
            "standard": ("Standard Shipping", StandardShipping),
            "express": ("Express Shipping", ExpressShipping),
            "pickup": ("In-Store Pickup", InStorePickup)
        }

        frame_payment = tk.LabelFrame(self, text="Payment Methods")
        frame_payment.pack(pady=10)

        for value, (text, _) in self.payment_methods.items():
            radiobutton = tk.Radiobutton(frame_payment, text=text, variable=self.selected_payment,value=value, anchor="w")
            radiobutton.pack(fill="both", padx=10, pady=5)

        frame_shipping = tk.LabelFrame(self, text="Shipping Methods")
        frame_shipping.pack(pady=10)

        for value, (text, _) in self.shipping_methods.items():
            radiobutton = tk.Radiobutton(frame_shipping, text=text, variable=self.selected_shipping, value=value, anchor="w")
            radiobutton.pack(fill="both", padx=10, pady=5)

        btn_checkout = tk.Button(self, text="Pay", command=self.process_checkout)
        btn_checkout.pack(pady=10)

        btn_back = tk.Button(self, text="Back", command=lambda: controller.show_frame("MainPage"))
        btn_back.pack(pady=10)

    def process_checkout(self):
        if not self.controller.client.cart:
            messagebox.showerror(title=None, message="Your cart is empty.")
            return

        payment_method = self.selected_payment.get()
        shipping_method = self.selected_shipping.get()

        if not payment_method:
            messagebox.showerror(title=None, message="Please select a payment method.")
            return

        if not shipping_method:
            messagebox.showerror(title=None, message="Please select a shipping method.")
            return

        payment_class = self.payment_methods[payment_method][1]
        shipping_class = self.shipping_methods[shipping_method][1]

        total_amount, total_weight = self.controller.client.calculate_totals()
        payment_instance = payment_class()
        total_with_discount = process_payment(payment_instance, total_amount)

        shipping_instance = shipping_class()
        shipping_cost = calculate_shipping(shipping_instance, total_weight, self.controller.client.client_distance_from_store, len(self.controller.client.cart))
        total_amount_with_shipping = total_with_discount + shipping_cost

        summary_message = (
            f"Amount with discount: ${total_with_discount:.2f}\n"
            f"Shipping Cost: ${shipping_cost:.2f}\n"
            f"Amount Paid: ${total_amount_with_shipping:.2f}"
        )

        messagebox.showinfo(title="Checkout Summary", message=summary_message)
        
        confirm = messagebox.askyesno(title=None, message=f"Are you sure you want to pay ${total_amount_with_shipping:.2f}?")
        if not confirm:
            return

        self.controller.client.cart.clear()
        save_pickle_file(self.controller.client, f"{self.controller.client.client_email}.pickle")
