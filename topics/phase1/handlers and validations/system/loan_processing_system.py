from factories.handler_factory import HandlerFactory
class System:
    def __init__(self,analyzer,payment,notifier,decision_engine):
        self.analyzer = analyzer
        self.payment = payment
        self.notifier = notifier
        self.decision_engine = decision_engine
    def run(self):
        handler_factory = HandlerFactory(payment=self.payment,notifier=self.notifier)
        result = self.analyzer.analyze()
        print(f"Analysis Result: {result}")
        if("fraud_probability" in result and isinstance(result["fraud_probability"],(int,float)) and 0 <= result["fraud_probability"] <= 1):
              
              decision = self.decision_engine.decide(result)
              print(f"Decision: {decision}")
              handler = handler_factory.get_handler(decision["decision_type"])
              print(f"Handler: {handler.__class__.__name__}")
              handler.handle()
        else:              
            print("Invalid analysis result: Missing or invalid 'fraud_probability'")