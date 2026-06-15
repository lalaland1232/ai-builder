from sqlalchemy import Column, Integer, String,create_engine
from sqlalchemy.orm import declarative_base , Mapped , mapped_column , Session
engine=create_engine("sqlite:///database.db")
Base = declarative_base()
class User(Base):
    __tablename__ = "users"
    id:Mapped[int]=mapped_column(Integer,primary_key=True)
    name:Mapped[str]=mapped_column(String,nullable=False)
    email:Mapped[str]=mapped_column(String,nullable=False,unique=True)
    
Base.metadata.create_all(engine)
session = Session(engine)