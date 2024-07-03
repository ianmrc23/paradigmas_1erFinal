from abc import ABC, abstractmethod


class PaymentMethod(ABC):
    """
    Clase abstracta para definir un método de pago.
    """
    @abstractmethod
    def process_payment(self, amount: float) -> float:
        pass


class CashPayment(PaymentMethod):
    """
    Método de pago en efectivo.
    """

    def process_payment(self, amount: float) -> float:
        return amount


class CardPayment(PaymentMethod):
    """
    Método de pago con tarjeta.
    """

    def process_payment(self, amount: float) -> float:
        return amount * 0.7


class QRPayment(PaymentMethod):
    """
    Método de pago con QR.
    """

    def process_payment(self, amount: float) -> float:
        return amount * 0.9


def process_payment(payment_method: PaymentMethod, total_amount: float) -> float:
    """
    Procesa el pago usando el método de pago especificado.
    """
    return payment_method.process_payment(total_amount)


class ShippingMethod(ABC):
    """
    Clase abstracta para definir un método de envío.
    """
    @abstractmethod
    def calculate_shipping_cost(self, weight: float, distance_from_store: float, total_products: int) -> float:
        pass


class StandardShipping(ShippingMethod):
    """
    Método de envío estándar.
    """

    def calculate_shipping_cost(self, weight: float, distance_from_store: float, total_products: int) -> float:
        return 5 + weight * 0.5 + distance_from_store * 0.1


class ExpressShipping(ShippingMethod):
    """
    Método de envío exprés.
    """

    def calculate_shipping_cost(self, weight: float, distance_from_store: float, total_products: int) -> float:
        return 10 + weight + distance_from_store * 0.2 + total_products * 0.2


class InStorePickup(ShippingMethod):
    """
    Método de recogida en tienda.
    """

    def calculate_shipping_cost(self, weight: float, distance_from_store: float, total_products: int) -> float:
        return 0


def calculate_shipping(
    shipping_method: ShippingMethod,
    weight: float,
    distance_from_store: float,
    total_products: int
) -> float:
    """
    Calcula el costo del envío usando el método de envío especificado.
    """
    return shipping_method.calculate_shipping_cost(weight, distance_from_store, total_products)
