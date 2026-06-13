from contracts.Notifier import Notifier
class WhatsAppNotifier(Notifier):
   
    def notify(self,message):
        print(f"WhatsApp Notification: {message}")
        