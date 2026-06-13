from contracts.Handler import Handler
class RejectedHandler(Handler):
    def __init__(self,notifier):
        self.notifier = notifier
    def handle(self):
       try:
          self.notifier.notify("Payment Rejected")
       except:
           return {
            "status": "error",
            "message": "Failed to send notification"
           }