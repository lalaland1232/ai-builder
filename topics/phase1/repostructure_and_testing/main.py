from systems.loan_processing_system import LoanProcessingSystem
from services.fake_approved_analyzer import FakeApprovedAnalyzer
from services.fake_rejected_analyzer import FakeRejectedAnalyzer
from services.fake_notifier import FakeNotifier
from services.fake_payment_processor import FakePaymentProcessor
approve_analyzer = FakeApprovedAnalyzer()
reject_analyzer = FakeRejectedAnalyzer()
payment = FakePaymentProcessor()
notifier = FakeNotifier()
loanprocessing1 = LoanProcessingSystem(analyzer=approve_analyzer, paymentprocessor=payment,notifier=notifier)
loanprocessing2=LoanProcessingSystem(analyzer=reject_analyzer, paymentprocessor=payment,notifier=notifier)
loanprocessing1.run()
print(notifier.called)
print(payment.called)
loanprocessing2.run()
print(notifier.called)
print(payment.called)