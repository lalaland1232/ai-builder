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
    try:
        response=requests.post(url,headers={
            "Authorization":f"Bearer {api_key}",
            "Content-Type":"application/json"
        },json={
            "model":"openai/gpt-4o-mini",
            "messages":[{"role":"user","content":prompt}]
        })
    except:
        return {
            "error":True,
            "message":"Failed to connect to OpenAI API",
        }
    if response.status_code == 200:
        result = response.json()
        content = result['choices'][0]['message']['content']
        try :
            return json.loads(content)
        except:
            return {
                "error":True,
                "message":"Failed to parse JSON from response",}



def trigger_alert(data):
    if data.get("error"):
        return {
            "alert":False,
            "devices":0,
            "reason":"Failed to analyze health data",
            "inform_hospital":False
        }
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