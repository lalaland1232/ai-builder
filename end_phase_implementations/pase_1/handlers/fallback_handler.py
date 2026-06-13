from base.base_handler import BaseHandler
class FallbackHandler(BaseHandler):
    def __init__(self,notifier,ai_service,prompt,analysis_result):
        self.notifier=notifier
        self.ai_service=ai_service
        self.prompt=prompt
        self.analysis_result=analysis_result
    def validate(self):
        if self.analysis_result.estimated_tokens > 0:
            self.is_validate=True
        else:
            self.is_validate=False
    def execute(self):
        if self.is_validate:
            self.response=self.ai_service.generate_response(prompt=self.prompt,model_name="openai/pt-turbo-16k")
        
    def postprocess(self):
        if self.response and self.response.status_code == 200:
            try:
                response_data = self.response.json()
                generated_content = response_data['choices'][0]['message']['content']
                print("Generated Content:", generated_content)
                self.notifier.send("Content is allowed and has been processed.")
            except Exception as e:              
                print(f"Error processing response: {e}")