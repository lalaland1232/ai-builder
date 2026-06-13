from contracts.Payment import Payment
class RazorPayPaymentProcessor(Payment):
    def __init__(self):
        self.called = False
    def process_payment(self):
        self.called = True
        