import requests
import json
import os
api_key=os.getenv("OPENROUTER_API_KEY")
url ="https://openrouter.ai/api/v1/chat/completions"


def trigger_alert(data):
    if (data["severity"]=="high" and data["probability"]>0.3) or (data["severity"]=="medium" and data["probability"]>0.6):
        return {
            "alert":True,
            "severity":data["severity"],
            "probability":data["probability"],
            "reason": "High severity with required probablity"  if data["severity"]== "high" else "Medium severity with required  probability"
        } 
    else:        return {
            "alert":False,
            "severity":data["severity"],
            "probability":data["probability"]
    }
prompt="""
    Role:ai health analyzer 
    Task: analyze health according to symptoms and generate output
    context:{
        symptoms:["fever","chest pain"],
        blood_pressure:150,
        heartrate:110,
        energy:very low
    }
    Constraints:
- Return ONLY JSON
- No explanation
- No markdown
- Follow schema exactly
   
    output:json{
        "severity":[high,medium,low],
        "probability":(0-1);
        "type of disease":"",
        relatedToOrgan:""
    }
"""
response=requests.post(url,headers={
        "Authorization": f"Bearer {api_key}",
        "Content-Type": "application/json"
    },json={
        "model":"openai/gpt-4o-mini",
        "messages":[{"role":"user","content":prompt}]
    })
result=response.json()
print(result)
ai_text=result["choices"][0]["message"]["content"]

ai_text_data=json.loads(ai_text)
print(ai_text_data)
alert=trigger_alert(ai_text_data)
print(alert)