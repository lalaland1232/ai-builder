import json
import requests
import os

api_key=os.getenv("OPENAI_API_KEY")
print("API Key:", api_key)
def healt_analyze():
    prompt = """
    Role: Health Analyzer AI

    Task:
    Analyze symptoms and return ONLY valid JSON.

    Context:
    {
    "symptoms": ["vomit", "blood vomit", "low energy"],
    "blood_pressure": 120,
    "heart_rate": 72
    }

    Output:
    {
    "severity": "low | medium | high",
    "probability": 0.0
    }
    """

    url = "https://openrouter.ai/api/v1/chat/completions"
    response=requests.post(url,headers={
        "Authorization":f"Bearer {api_key}",
        "Content-Type":"application/json"
    },json={
        "model":"openai/gpt-4o-mini",
        "messages":[{"role":"user","content":prompt}]
    })
    result=response.json()["choices"][0]["message"]["content"]
    return json.loads(result)



def trigger_alert(data):
    if(data["severity"]=="high" and data["probability"]>0.3) or (data["severity"]=="medium" and data["probability"]>0.6):
        print("Alert triggered with severity:", data["severity"], "and probability:", data["probability"])
        return {
            "alert":True,
            "devices":[{ "type":"mobile","id":1 },{ "type":"tablet","id":2 }],
            "reason":"High severity with required probablity"  if data["severity"]== "high" else "Medium severity with required  probability",
            "inform_hospital":False
        }
    else:
        print("No alert triggered. Severity:", data["severity"], "Probability:", data["probability"])
        return {
            
            "alert":False,
            "devices":0,
            "reason":"No alert triggered",
            "inform_hospital":False
        }
def send_notification(alert):
    if alert["alert"]:
        for device in alert["devices"]:
            print("notification sent to ",device["type"])
    else:
        print("No notification sent. Reason:", alert["reason"])
data=healt_analyze()
alert=trigger_alert(data)
send_notification(alert)