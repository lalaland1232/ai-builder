from contracts.Analyzer import Analyzer
class FraudAnalyzer(Analyzer):
    def analyze(self):
        return{
    "fraud_probability": 0.9
}