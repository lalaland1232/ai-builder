from sqlalchemy.orm import (Mapped, mapped_column, relationship,Session,DeclarativeBase)
from sqlalchemy import String, Integer, ForeignKey, create_engine, select
class Base(DeclarativeBase):
    pass
engine = create_engine("sqlite:///:memory:")

class User(Base):
    __tablename__ = "users"
    id:Mapped[int]=mapped_column(Integer,primary_key=True)
    name:Mapped[str]=mapped_column(String , nullable=False)
    email:Mapped[str]=mapped_column(String , nullable=False,unique=True)
    agents:Mapped[list["Agent"]]=relationship(back_populates="user")
class Agent(Base):
    __tablename__ = "agents"
    id:Mapped[int]=mapped_column(Integer,primary_key=True)
    user_id:Mapped[int]=mapped_column(Integer,ForeignKey("users.id"))
    name:Mapped[str]=mapped_column(String , nullable=False)
    user:Mapped["User"]=relationship(back_populates="agents")

Base.metadata.create_all(engine)
session=Session(engine)
user = User(
    name="Baba",
    email="baba@example.com"
)
print("before adding:", user.id)
session.add(user)
print("after adding:", user.id)
session.commit()
print("after commit:", user.id)
agent = Agent(
    name="Research Agent",
    user_id = user.id
)
session.add(agent)
session.commit()
print("Agent ID:", agent.id)
print("Agent's User ID:", agent.user_id)
stmt = select(User)
result=session.execute(stmt)

user = result.scalars().all()
print(user[0].name)
print(user[0].email)