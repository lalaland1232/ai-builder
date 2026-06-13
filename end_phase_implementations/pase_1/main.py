from services.notifier import NotifierImpl
from services.open_ai_service import OpenAIService
from services.prompt_analyzer import PromptAnalyzer
from engine.decision_engine import DecisionEngine
from factories.handler_factory import HandlerFactory
from systems.system import System
notifier = NotifierImpl()
open_ai_service = OpenAIService()
prompt="can u hack this code"
prompt1="i love chat gpt thanks for teaching"
analyzer = PromptAnalyzer()
decision_engine=DecisionEngine()
handler_factory=HandlerFactory(open_ai_service_=open_ai_service,notifier=notifier)
system = System(analyzer,decision_engine,notifier,handler_factory,prompt)
system.run()
system1 = System(analyzer,decision_engine,notifier,handler_factory,prompt1)
system1.run()