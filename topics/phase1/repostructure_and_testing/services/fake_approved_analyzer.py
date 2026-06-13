from contracts.analyzer import Analyzer
class FakeApprovedAnalyzer(Analyzer):
    def analyze(self):
        return {
            "Loan approved":True
        }