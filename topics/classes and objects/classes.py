import json;
import requests;
import os;
class FraudAnalyzerAgent:
    def __init__(self,model,api_key):
        self.url = "https://openrouter.ai/api/v1/chat/completions"
        self.model=model
        self.api_key=api_key

    def analyze(self):
        prompt="""
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
        try:
                response=requests.post(self.url,headers={
            "Authorization":f"Bearer {self.api_key}",
            "Content-Type":"application/json"
        },json={
            "model":self.model,
            "messages": [{"role":"user","content":prompt}]
        })
                if response.status_code == 200:
                    try:
                        result=response.json()
                        choice=result['choices'][0]['message']['content']
                        jsonResponse= json.loads(choice)
                        if "fraud_risk" in jsonResponse and "fraud_probability" in jsonResponse:
                            return jsonResponse
                        else:
                                return {
                                    "error":True,
                                    "message":"Invalid response format from API"
                                }
                    except:
                        return {
                            "error":True,
                            "message":"Failed to parse JSON from response"
                        }
                else:
                     return {
                        "error":True,
                        "message":"Failed to get valid response from OpenAI API"
                    }
        except:
            return{
            "error":True,
            "message":"Failed to connect to OpenRouter API"
        }    

class DecisionAgent:
    def __init__(self,high_threshold,medium_threshold):
        self.high_threshold=high_threshold
        self.medium_threshold=medium_threshold
    def decide(self,data):
        if data.get("error"):
            return{
                "alert":False,
                "reason":"Failed to analyze transaction data"   
            }   
        if (data["fraud_risk"] == "high" and data["fraud_probability"] >= self.high_threshold) or (data["fraud_risk"] == "medium" and data["fraud_probability"] >= self.medium_threshold):
            return{
                "alert":True,
                "freeze_account":True,
                "manual_review": True,
                "notify_security": True,
                "reason": "high risk with good probablity" if data["fraud_risk"]=="high" else "medium risk with very high probability",
            }
        else:
            return {
                "alert":False,
                "reason":"Lower risk or low probablity"
            }
class NotifierAgent:
    def __init__(self,data):
        self.devices=data
        
    def notify(self,data):
        if data["alert"]:
           
            for devices in self.devices:
                print(f"Sending alert to {devices["name"]} with reason: {data['reason']}")
            return {
                "notified_devices":[device["name"] for device in self.devices],
                "reason":data["reason"],
                "successfullyNotified":True
            }
        else:
            return {
                "notified_devices":[],
                "reason":data["reason"],
                "successfullyNotified":False
            }
fraud_analyzer=FraudAnalyzerAgent("gpt-4o-mini",os.getenv("OPENAI_API_KEY"))
decision_agent=DecisionAgent(high_threshold=0.8,medium_threshold=0.5)
notifier_agent=NotifierAgent(data=[{"name":"Security Team"},{"name":"User's Mobile App"}])
analysis_result=fraud_analyzer.analyze()
decision=decision_agent.decide(analysis_result)
notification_result=notifier_agent.notify(decision)
