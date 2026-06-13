from abc import ABC, abstractmethod
class DecisionEngineContract(ABC):
    @abstractmethod
    def make_decision(self,analysis_result):
        pass