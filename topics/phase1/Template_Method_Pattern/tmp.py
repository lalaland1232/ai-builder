import json
import os
import requests
class BaseAIAgent:
    def __init__(self,model,api_key):
        self.model=model
        self.api_key=api_key
        self.url="https://openrouter.ai/api/v1/chat/completions"
    def get_prompt(self):
        raise NotImplementedError("get_prompt() not implemented")
    def expected_keys(self):
        raise NotImplementedError("expected_keys() not implemented")
    
    def ask_ai(self):
        try:
            response=requests.post(self.url,headers={
                "Authorization":f"Bearer {self.api_key}",
                "Content-Type":"application/json"
            },json={
                "model":self.model,
                "messages":[{"role":"user","content":self.get_prompt()}]
            })
            if response.status_code == 200:
                try:
                    result=response.json()
                    choice = result['choices'][0]['message']['content']
                    jsonResponse = json.loads(choice)
                    return jsonResponse
                except:
                    return {
                        "error":True,
                        "reason":"error while parsing json"
                    }
            else:
                return {
                    "error":True,
                    "reason":response.json(),
                    "status_code":response.status_code
                }
        except:
            return {
                "error":True,
                "reason":"error while api call"
            }

    def analyze(self):
        result =self.ask_ai()
        print(result)
        if result.get("error"):
            return result
        else:
            for key in self.expected_keys():
                if key not in result:
                    return {
                        "error":True,
                        "reason":"missing expected key in response",
                        "missing_key":key
                    }
            print("success")
            print(result)
            return result
class FraudAnalyzerAgent(BaseAIAgent):
    def get_prompt(self):
        return """
                role: fraud analyzer;
task: analyze given transaction and predict if its fraudulent or not
context:{
   "transaction_amount": 85000,
   "location": "Russia",
   "usual_location": "India",
   "device_change": True,
   "login_attempts": 5
}
constraints:return only json
no marksdown
output : {
   "fraud_risk": "low | medium | high",
   "fraud_probability": 0.0,
   "reason": ""
}

                """
    def expected_keys(self):
        return [
            "fraud_risk","fraud_probability"
        ]
    def analyze(self):
        return super().analyze()
fraud_analyzer =FraudAnalyzerAgent(model="gpt-4o-mini",api_key=os.getenv("OPENAI_API_KEY"))
print(fraud_analyzer.analyze())
print("error")