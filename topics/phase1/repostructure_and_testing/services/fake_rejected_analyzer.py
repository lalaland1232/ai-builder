from contracts.analyzer import Analyzer
class FakeRejectedAnalyzer(Analyzer):
    def analyze(self):
        return {
            "Loan approved":False
        }