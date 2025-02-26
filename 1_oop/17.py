# ========= Zadanie 17 =============
from abc import ABC, abstractmethod


class PaymentProcessor(ABC):
    @abstractmethod
    def authorize_payment(self) -> None:
        pass

    @abstractmethod
    def capture_payment(self) -> None:
        pass

class CreditCardPayment(PaymentProcessor):
    def authorize_payment(self) -> str:
        return "Authorize credit card payment"

    def capture_payment(self) -> str:
        return "Capture credit card payment"


class PayPalPayment(PaymentProcessor):
    def authorize_payment(self) -> str:
        return "Authorize PayPal payment"

    def capture_payment(self) -> str:
        return "Capture PayPal payment"

print(CreditCardPayment().authorize_payment())
print(CreditCardPayment().capture_payment())
print(PayPalPayment().authorize_payment())
print(PayPalPayment().capture_payment())