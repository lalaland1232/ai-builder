from contracts.Handler import Handler
class ManualReviewHandler(Handler):
    def __init__(self,notifier):
        self.notifier = notifier
    def handle(self):
       try:
          self.notifier.notify("Transaction flagged for manual review.")
       except:
           return {
            "status": "error",
            "message": "Failed to send notification"
           }