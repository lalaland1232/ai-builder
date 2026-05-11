import requests
import os
import json

api_key = os.getenv("OPENAI_API_KEY")
print("API Key:", api_key)
def ai_analyzer():
    url="https://openrouter.ai/api/v1/chat/completions"; 
    prompt="""
    role: stock analyzer;
    task: analyze given stock and predict its rise or fall
    context:{
    
        "stock":"Tesla",
   "current_price":240,
   "news":"Tesla facing production delays and weak quarterly guidance"
   }
   constraints:return only json
    no marksdown
    output : {
   "risk":"low | medium | high",
   "drop_probability":0.0
    }


"""
    try:
        response=requests.post(url,headers=
        {
            "Authorization":f"Bearer {api_key}",
            "Content-Type":"application/json"
        },json={
            "model":"openai/gpt-4o-mini",
            "messages":[{"role":"user","content":prompt}]
        })
    except:
        return {
            "error":True,
            "message":"Failed to connect to OpenAI API"
        }
    if response.status_code == 200:
        result = response.json()
        choice=result['choices'][0]['message']['content']
        try:
            return json.loads(choice)
        except:
            return {
                "error":True,
                "message":"Failed to parse JSON from response"
            }
    else : 
        print("API Error:", response.status_code, response.text)
        return {
                "error":True,
                "message":"Failed to parse JSON from response"
            }

def decision_engine(data) :
    if data.get("error"):
        return {
            "alert":False,
            "reason":"Failed to analyze stock data",
            "inform_investor":False
        }
    if data["risk"]=="high" and data["drop_probability"]>0.4 or data["risk"]=="medium" and data["drop_probability"]>0.7:
        return {
            "alert":True,
            "reason":"High risk with required drop probability" if data["risk"]=="high" else "Medium risk with required drop probability",
            "inform_investor":True,
            "devices":[{"type":"mobile" , "platform":"iOS"},{"type":"tablet" , "platform":"Android"},{"type":"laptop" , "platform":"Windows"}]
        }
    else:
        return {
            "alert":False,
            "reason":"No alert triggered",
            "inform_investor":False
        }
def notifier(data):
    if data["alert"]== False:
        print("No alert triggered. Reason:", data["reason"])
    else:
        for device in data["devices"]:
            print(f"Sending alert to {device['type']} on {device['platform']} platform. Reason: {data['reason']}")
    
    
result = ai_analyzer()

decision = decision_engine(result)
notifier(decision)