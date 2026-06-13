from contracts.handler import BaseHandler
from abc import ABC, abstractmethod
class BaseHandler(
    BaseHandler , ABC):
    def handle(self):
        self.preprocess()
        self.validate()
        self.execute()
        self.postprocess()
    
    def preprocess(self):
        pass
    def postprocess(self):
        pass 
    @abstractmethod
    def validate(self):
        pass
    @abstractmethod
    def execute(self):
        pass  
