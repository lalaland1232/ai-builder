from contracts.notifier import Notifier
class NotifierImpl(Notifier):
    def send(self,message):
        print(f"Notification: {message}")