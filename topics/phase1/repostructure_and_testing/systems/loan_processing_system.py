class LoanProcessingSystem:
    def __init__ (self,analyzer,notifier,paymentprocessor):
        
        self.analyzer=analyzer
        self.notifier=notifier
        self.paymentprocessor=paymentprocessor
    
    def run(self):
    
        if self.analyzer.analyze()["Loan approved"]:
            self.paymentprocessor.process_payment()
            self.notifier.notify()

        else:
            self.paymentprocessor.called=False
            self.notifier.called=False