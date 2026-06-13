from contracts.Handler import Handler
class ApprovedHandler(Handler):
    def __init__(self,payment,notifier):
        self.payment = payment
        self.notifier = notifier
    def handle(self):
      
       try:
          self.payment.process_payment()
          self.notifier.notify("Payment Approved")
       
       except:    
           
           return {
            "status": "error",
            "message": "Failed to process payment or send notification"
           }