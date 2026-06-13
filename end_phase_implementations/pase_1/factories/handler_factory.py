from handlers.allow_handler import AllowHandler
from handlers.block_handler import BlockHandler
from handlers.fallback_handler import FallbackHandler
class HandlerFactory:
    def __init__(self,notifier,open_ai_service_):
        self.notifier=notifier
        self.open_ai_service=open_ai_service_
        
        

    def get_handler(self,decision_result,analysis_result,prompt):
        if decision_result.action == "ALLOW":
            return AllowHandler(analysis_result=analysis_result,notifier=self.notifier,open_ai_service=self.open_ai_service,prompt=prompt)
        elif decision_result.action == "BLOCK":
            return BlockHandler(notifier=self.notifier)
        elif decision_result.action == "FALLBACK":
            return FallbackHandler(notifier=self.notifier,ai_service=self.open_ai_service,prompt=prompt,analysis_result=analysis_result)
        
    