def healt_analyze():
    return {

    "severity":"high",
    "probability":0.8,
    }
def trigger_alert(data):
    if(data["severity"]=="high" and data["probability"]>0.3) or (data["severity"]=="medium" and data["probability"]>0.6):
        return {
            "alert":True,
            "devices":[{ "type":"mobile","id":1 },{ "type":"tablet","id":2 }],
            "reason":"High severity with required probablity"  if data["severity"]== "high" else "Medium severity with required  probability",
            "inform_hospital":False
        }
    else:
        return {
            "alert":False,
            "devices":0,
            "reason":"No alert triggered",
            "inform_hospital":False
        }
data=healt_analyze()
alert=trigger_alert(data)
print(alert)