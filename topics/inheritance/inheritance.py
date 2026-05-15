import os

import json
import requests
class BaseAIAgent:
    def __init__(self,model,api_key):
        self.model=model
        self.api_key=api_key
        self.url="https://openrouter.ai/api/v1/chat/completions"
    def ask_ai(self,prompt):
            try: 
                response=requests.post(self.url,headers={
                    "Authorization":f"Bearer {self.api_key}",
                    "Content-Type":"application/json"
                },json={
                    "model":self.model,
                    "messages": [{"role":"user","content":prompt}]
                })
                if response.status_code ==200:
                    try:
                        result=response.json()
                        choice=result['choices'][0]['message']['content']
                        return json.loads(choice)
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
            except :
                return {
                    "error":True,
                    "message":"Exception occurred while connecting to OpenAI API"
                }

class FraudAnalyzerAgent(BaseAIAgent):
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
        result=self.ask_ai(prompt)
        if result.get("error"):
            return result
        if "fraud_risk" in result and "fraud_probability" in result:
            return result
        else:            
            return {
                "error":True,
                "message":"Invalid response format from API format: \n missing keys: { 'fraud_risk' in result}, {'fraud_probability' in result}"
            }
class LoananalyzerAgent(BaseAIAgent):
    def analyze(self):
        prompt="""
            role: loan application analyzer;
            task: analyze given loan application and predict if it should be approved or not
        context:{
        "applicant_income": 1200000,
        "credit_score": 750,
        "loan_amount": 50000,
        "loan_purpose": "home improvement",
        "employment_status": "employed"
        }
        constraints:return only json
        no marksdown
        output : {
        "approval_status": "approved | rejected",
        "approval_probability": 0.0,
        "reason": "",
        "loan_risk": "low | medium | high",
        "default_probability": 0.0

        }
        """
        result=self.ask_ai(prompt)
        if result.get("error"): 
            return result
        if "loan_risk" in result and "default_probability" in result:
            return result
        else:            
            return {
                "error":True,
                "message":"Invalid response format from API format: \n missing keys: { 'loan_risk' in result}, {'default_probability' in result}"
            }
class FraudDecisionmaker:
    def __init__(self,highThreshold,midThreshhold):
        self.highThreshold=highThreshold
        self.midThreshhold=midThreshhold
    def make_decision(self,fraud_analysis):
        
        if fraud_analysis.get("error"):
            return {
                "alert":False,
                "reason":f"Cannot make decision due to error in analysis: {fraud_analysis['message']}"
            }
        
        if (fraud_analysis["fraud_risk"]=="high" and fraud_analysis["fraud_probability"]>=self.highThreshold) or (fraud_analysis["fraud_risk"]=="medium" and fraud_analysis["fraud_probability"]>=self.midThreshhold):
        
            return {
                "alert":True,
                "reason":f"Transaction flagged as potentially fraudulent with risk level {fraud_analysis['fraud_risk']} and probability {fraud_analysis['fraud_probability']}"
            }
        else:
            return {
                "alert":False,
                "reason":f"Transaction considered low risk with risk level {fraud_analysis['fraud_risk']} and probability {fraud_analysis['fraud_probability']}"
            }
class LoanDecisionmaker:
    def __init__(self,highThreshold,mediumThreshold):
        self.highThreshold=highThreshold
        self.mediumThreshold=mediumThreshold
    def make_decision(self,loan_analysis):
        print(loan_analysis)
        if loan_analysis.get("error"):
            return {
                "approval":False,
                "reason":f"Cannot make decision due to error in analysis: {loan_analysis['message']}"
            }
        
        if (loan_analysis["loan_risk"]=="high" and loan_analysis["default_probability"]>=self.highThreshold) or (loan_analysis["loan_risk"]=="medium" and loan_analysis["default_probability"]>=self.mediumThreshold):
        
            return {
                "alert":True,
                "reason":f"Loan rejected due to high risk level {loan_analysis['loan_risk']} and default probability {loan_analysis['default_probability']}"
            }
        else:
            return {
                "alert":False,
                "reason":f"Loan approved with approval probability {loan_analysis['approval_probability']} and risk level {loan_analysis['loan_risk']}"
            }
class Notifier:
    def __init__(self,devices):
        self.devices=devices
    def notify(self,decision):
        if decision["alert"]:
            for device in self.devices:
                print(f"Sending alert to {device['name']} with reason: {decision['reason']}")
            return {
                "notified":True,
                "devices_notified":[device["name"] for device in self.devices],
                "reason":decision["reason"]
            }
        else:
            print("loan approvved client can get load")
            return {
                "notified":False,
                "reason":decision["reason"]
            }
fraud_agent=FraudAnalyzerAgent("gpt-4o-mini",os.getenv("OPENAI_API_KEY"))
decision_maker_fraudDetection=FraudDecisionmaker(highThreshold=0.5,midThreshhold=0.8)
notifyOrNot=decision_maker_fraudDetection.make_decision(fraud_agent.analyze())
notifier_fraud=Notifier([{"name":"Security Team"},{"name":"User's Mobile App"}])
notifier_fraud.notify(notifyOrNot)
loan_agent=LoananalyzerAgent("gpt-4o-mini",os.getenv("OPENAI_API_KEY"))
decision_maker_loanApproval=LoanDecisionmaker(highThreshold=0.5,mediumThreshold=0.8)
notifyOrNot_loan=decision_maker_loanApproval.make_decision(loan_agent.analyze())
notifier_loan=Notifier([{"name":"Loan Officer"},{"name":"Applicant's Email"}])