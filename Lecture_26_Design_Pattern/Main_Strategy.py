from abc import ABC, abstractmethod

class PaymentStrategy(ABC):
    @abstractmethod
    def pay(self, amount: float):pass

class CreditCardPayment(PaymentStrategy):    
    def pay(self, amount: float):
        print(f"Paid ${amount} via Credit Card")

class CryptoPayment(PaymentStrategy):    
    def pay(self, amount: float):
        print(f"Paid ${amount} via Crypto")


class ShoppingCart:
    def __init__(self, strategy: PaymentStrategy):
        self.strategy = strategy

    def checkout(self, amount: float):
        self.strategy.pay(amount)


cart = ShoppingCart(CreditCardPayment())
cart.checkout(100.0)

cart.strategy = CryptoPayment()
cart.checkout(100.0)