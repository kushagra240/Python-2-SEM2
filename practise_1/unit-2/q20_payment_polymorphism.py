class Payment:
    def pay(self):
        print("Payment made")


class CreditCardPayment(Payment):
    def pay(self):
        print("Paid using credit card")


class UPIPayment(Payment):
    def pay(self):
        print("Paid using UPI")


for payment in (CreditCardPayment(), UPIPayment()):
    payment.pay()