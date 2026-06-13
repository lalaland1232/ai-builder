from user.repository import UserRepository
from agents.repository import AgentRepository
from models import session,User,Agent
class AgentService:
    user_repository=UserRepository(session)
    agent_repository=AgentRepository(session)
    def create_user_with_agent(self,name,email,agent_name):
        try:
            if self.user_repository.get_by_email(email):
                print("User with this email already exists.")
                return
            user = User(name=name,email=email)
            agent = Agent(name=agent_name)
            agent.user=user
            self.user_repository.create_user(user)
            self.agent_repository.create_agent(agent)
            session.commit()
        except Exception as e:
            session.rollback()
            print(f"Error creating user and agent: {e}")