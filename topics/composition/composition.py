import os
import requests
import json

class FraudMonitoringSystem:
    def run(self):
        analysis=self.analyzer.analyzes()
        decision = self.decision_engine.make_decision(analysis)
        notification = self.notifier(decision)
        return notification 
class FakeAnalyzer:
    def analyze(self):
        return {
   "fraud_risk": "high",
   "fraud_probability": 0.95
}