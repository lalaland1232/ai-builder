from contracts.paymentprocessor import PaymentProcessor
class FakePaymentProcessor(PaymentProcessor):
    def __init__(self):
        self.called=False
    def process_payment(self):
        self.called=True