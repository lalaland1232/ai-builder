from abc import ABC ,abstractmethod

class Analyzer(ABC):
    @abstractmethod
    def analyze(self):
        pass

class Success(Analyzer):
    def analyze(self):
        pass
class Fail(Analyzer):
    pass

try:
    success= Success()
    print("object created successfully")
except:
    pass


try:
    fail= Fail()
    print("object created successfully")
except:
    print("object creation failed as it didnt have requried methods")