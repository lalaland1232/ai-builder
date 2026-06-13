class System:
    def __init__(self,analyzer,decision_engine,notifier,handler_factory,prompt):
        self.analyzer = analyzer
        self.decision_engine = decision_engine
        self.notifier = notifier
        self.handler_factory = handler_factory
        self.prompt = prompt

    
    def run(self):
        analysis=self.analyzer.analyze(self.prompt)
        decision=self.decision_engine.make_decision(analysis)
        handler=self.handler_factory.get_handler(decision,analysis,prompt=self.prompt)
        handler.handle()