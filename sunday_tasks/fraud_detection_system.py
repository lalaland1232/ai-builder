import requests
import json 
import os
api_key=os.getenv("OPENAI_API_KEY")
def faurd_analyzer():
    url="https://openrouter.ai/api/v1/chat/completions"
    promt="""
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
        response=requests.post(url,headers={
            "Authorization":f"Bearer {api_key}",
            "Content-Type":"application/json"
        },json={
            "model":"openai/gpt-4o-mini",
            "messages": [{"role":"user","content":promt}]
        })
        if response.status_code != 200:
            print("API Error:", response.status_code, response.text)
            return {
                "error":True,
                "message":"Failed to get valid response from OpenAI API"
            }
        try:
            result=response.json()
            
            choice=result['choices'][0]['message']['content']
            
            jsonResponse= json.loads(choice)
            
            return jsonResponse
        except:
            return {
                "error":True,
                "message":"Failed to parse JSON from response"
            }
    except:
        return{
            "error":True,
            "message":"Failed to connect to OpenAI API"
        } 
    
def decision_engine(data):
    if data.get("error"):
        return{
            "alert":False,
            "reason":"Failed to analyze transaction data"   
        }
    if "fraud_risk" in data and "fraud_probability" in data:
        if (data["fraud_risk"]=="high" and data["fraud_probability"] > 0.5 ) or (data["fraud_risk"]=="medium" and data["fraud_probability"] > 0.8):
            return {
                    "alert":True,
                    "freeze_account":True,
                    "manual_review": True,
                    "notify_security": True,
                    "reason": "high risk with good probablity" if data["fraud_risk"]=="high" else "medium risk with very high probability",
                    "devices": [{"id": "device1","type":"mobile"},{"id": "device2","type":"desktop"}]
                    }
        else:
            return {
                    "alert":False,
                    "freeze_account":False,
                    "manual_review": False,
                    "notify_security": False,
                    "reason": "No alert triggered. Risk: {} with Probability: {}".format(data["fraud_risk"], data["fraud_probability"])
                }
    else:
        return {
        "alert":False,
        "reason":"not proper information retrived",
        "inform_bank":False
    }

def notifier(data):
    if not data.get("alert")  :
        print("No alert to notify. Reason:", data.get("reason"))
        return {
            "notification_sent":False,
            "reason":"No alert to notify"
        }
    if data.get("manual_review"):
        for devide in data["devices"]:
            print("Notification sent to security team for device:", devide["id"], "of type:", devide["type"])
        return {
            "notification_sent":True,
        }
    else:
        print("please perform manual varification first")
        return {
            "notification_sent":False,
            "reason":"Manual review required before notification"
            }
alert_data=faurd_analyzer()

decision=decision_engine(alert_data)
notifier(decision)