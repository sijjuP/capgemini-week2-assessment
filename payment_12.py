class Payment:
    def process_payment(self):
        print("Processing payment through UPI\n")

class CreditCardPayment(Payment):
    def process_payment(self):
        print("Processing payment through Credit card\n")

class PayPalPayment(Payment):
    def process_payment(self):
        print("Processing payment through Pay pal\n")

class BitcoinPayment(Payment):
    def process_payment(self):
        print("Processing payment through Bit coin\n")

card=CreditCardPayment()
card.process_payment()
paypal=PayPalPayment()
paypal.process_payment()
bit=BitcoinPayment()
bit.process_payment()