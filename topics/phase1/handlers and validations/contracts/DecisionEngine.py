from abc import ABC, abstractmethod
class DecisionEngine(ABC):
    @abstractmethod
    def decide(self):
        pass