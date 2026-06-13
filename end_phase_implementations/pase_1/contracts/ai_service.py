from abc import ABC, abstractmethod
class AIService(ABC):
    @abstractmethod
    def generate_response(self,model_name,prompt):
        pass