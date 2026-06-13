from contracts.analyzer import Analyzer
from models.analysis_result import AnalysisResult
class PromptAnalyzer(Analyzer):
    def analyze(self, prompt):
        blocked_words=["hack","malware","phishing"]
        number_of_blocked_words = 0
        for word in blocked_words:
            if word.lower() in prompt.lower():
                number_of_blocked_words += 1
        if number_of_blocked_words > 0:
            return AnalysisResult(estimated_tokens=len(prompt),contains_blocked_content=True,number_of_blocked_words=number_of_blocked_words)
        else:
            return AnalysisResult(estimated_tokens=len(prompt),contains_blocked_content=False,number_of_blocked_words=0)