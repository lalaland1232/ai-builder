from base.base_handler import BaseHandler
class BlockHandler(BaseHandler):
    def __init__(self,notifier):
        self.notifier=notifier
    def validate(self):
        pass
    def execute(self):
        self.notifier.send("Request blocked due to unsafe content")