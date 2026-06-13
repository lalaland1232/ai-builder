from contracts.DecisionEngine import DecisionEngine
class FraudDecisionEngine(DecisionEngine):
    def decide(self,analysis):
        if analysis["fraud_probability"] < 0.3:
            return {
                 "decision_type":"approved",
                "reason":"Low fraud probability"
            }
        elif analysis["fraud_probability"] > 0.3 and analysis["fraud_probability"] < 0.7:
            return {
               "decision_type":"manual_review",
                "reason":"Moderate fraud probability"
            }
        else:
            return {
                "decision_type":"rejected",
                "reason":"High fraud probability"
            }
