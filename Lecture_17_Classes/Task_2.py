class Payment:
    def process_payment(self, amount):
        print("payment is progress")

class CreditCardPayment(Payment):
    def process_payment(self, amount):
        print(f"{amount} GEL is payd by credit card")

class PayPalPayment(Payment):
    def process_payment(self, amount):
        print(f"{amount} GEL is payd by PayPalPayment")


credit_card_payment = CreditCardPayment()
credit_card_payment.process_payment(10)

paypal_payment = PayPalPayment()
paypal_payment.process_payment(20)