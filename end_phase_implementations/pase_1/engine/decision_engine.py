from contracts.decision_engine import DecisionEngineContract
from models.decision_result import DecisionResult
class DecisionEngine(DecisionEngineContract):
    def make_decision(self,analysis_result):
        if analysis_result.contains_blocked_content:
            return DecisionResult(action="BLOCK",reason=f"Content contains {analysis_result.number_of_blocked_words} blocked words.",notify=True)
        elif analysis_result.estimated_tokens > 1000:
            return DecisionResult(action="FALLBACK",reason=f"Content is too long with {analysis_result.estimated_tokens} tokens.",notify=True)
        else:
            return DecisionResult(action="ALLOW",reason="Content is acceptable.",notify=False)