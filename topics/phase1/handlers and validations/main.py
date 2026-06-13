from services.fakeanalyzer import FraudAnalyzer
from services.razor_pay_payment import RazorPayPaymentProcessor
from services.whatsapp_notifier import WhatsAppNotifier
from services.decision_engine import FraudDecisionEngine
from system.loan_processing_system import System
analyzer = FraudAnalyzer()
decision_engine = FraudDecisionEngine()
payment = RazorPayPaymentProcessor()
notifier = WhatsAppNotifier()
loan_system = System(analyzer=analyzer,payment=payment,notifier=notifier,decision_engine=decision_engine)
loan_system.run()