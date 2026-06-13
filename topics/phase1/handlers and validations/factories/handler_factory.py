from services.approved_handler import ApprovedHandler
from services.manual_review import ManualReviewHandler
from services.rejected_handler import RejectedHandler
class HandlerFactory:
    def __init__(self,notifier,payment):
        self.notifier = notifier
        self.payment = payment
    def get_handler(self,decision):
        if decision == "approved":
            return ApprovedHandler(notifier=self.notifier,payment=self.payment)
        elif decision == "manual_review":
            return ManualReviewHandler(notifier=self.notifier)
        else:
            return RejectedHandler(notifier=self.notifier)