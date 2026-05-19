from abc import ABC , abstractmethod
class Analyzer(ABC):
    @abstractmethod
    def analyze(self):
        pass

class Notifier(ABC):
    @abstractmethod
    def notify(self):
        pass

class PaymentProcessor(ABC):
    @abstractmethod
    def process_payment(self):
        pass

class LoanAnalyzer(Analyzer):
    def analyze(self):
        return {
            "Loan approved":True
        }
class EmailNotifier(Notifier):
    def notify(self):
        print("email sent")

class SMSNotifier(Notifier):
    def notify(self):
        print("SMS sent")

class RazorPayPayment(PaymentProcessor):
    def process_payment(self):
        print("payment processed through RazorPay")

class LoanProcessingSystem:
    def __init__(self,Analyzer,Notifier,PaymentProcessor):
        self.analyzer=Analyzer
        self.notifier=Notifier
        self.payment=PaymentProcessor
    
    def run(self):
        if self.analyzer.analyze()["Loan approved"]:
            self.payment.process_payment()
            self.notifier.notify()


system=LoanProcessingSystem(LoanAnalyzer(),EmailNotifier(),RazorPayPayment())
system.run()