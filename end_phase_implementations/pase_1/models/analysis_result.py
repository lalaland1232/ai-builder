class AnalysisResult:
    def __init__(self, estimated_tokens, contains_blocked_content, number_of_blocked_words):
        self.estimated_tokens = estimated_tokens
        self.contains_blocked_content = contains_blocked_content
        self.number_of_blocked_words = number_of_blocked_words
