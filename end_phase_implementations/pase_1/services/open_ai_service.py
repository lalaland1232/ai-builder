from contracts.ai_service import AIService
import json 
import os
import requests
class OpenAIService(AIService):
    def __init__(self):
        self.url="https://openrouter.ai/api/v1/chat/completions"
    def generate_response(self, model_name, prompt):
        try:
            response = requests.post(url=self.url,headers={
                "Authorization": f"Bearer {os.getenv('OPENAI_API_KEY')}",
                "Content-Type": "application/json"
            },json={
                "model":model_name,
                "messages": [
                    {"role": "user", "content": prompt}
                ]
            })
            return response
        except Exception as e:
            print(f"Error calling OpenAI API: {e}")