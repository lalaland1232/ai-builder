from models import Agent

class AgentRepository:
    def __init__(self,session):
        self.session = session
    
    def create_agent(self , agent : Agent):
        self.session.add(agent)

    def get_by_id(self , id:int):
        agent= self.session.get(Agent,id)
        if agent:
            return agent
        return None
    