from contracts.notifier import Notifier
class FakeNotifier(Notifier):
    def __init__(self):
        self.called=False
    def notify(self):
        self.called=True
        