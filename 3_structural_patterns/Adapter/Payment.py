class PayPal:
    def payment_method(self):
        return "Paying with PayPal"

class Stripe:
    def payment_method(self):
        return "Paying with Stripe"

class Adapter:
    def __init__(self, payPal:PayPal, stripe:Stripe):
        self.payPal = payPal
        self.stripe = stripe

    def payment_with_paypal(self):
        return self.payPal.payment_method()

    def payment_with_stripe(self):
        return self.stripe.payment_method()


paypal = PayPal()
stripe = Stripe()

adapter = Adapter(paypal, stripe)

print(adapter.payPal.payment_method())
print(adapter.stripe.payment_method())