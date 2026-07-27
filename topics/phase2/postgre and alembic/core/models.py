from core.database import Base
from sqlalchemy import Column,Integer,String,Boolean
from sqlalchemy.orm import relationship , Mapped , mapped_column
class User(Base):
    __tablename__="users"
    id:Mapped[int]=mapped_column(Integer,primary_key=True)
    email:Mapped[str]=mapped_column(String , nullable=False,unique=True)
    full_name:Mapped[str]=mapped_column(String,nullable=False)

class agent(Base):
    __tablename__="agents"
    id:Mapped[int]=mapped_column(Integer,primary_key=True)
    name: Mapped[str]=mapped_column(String,nullable=False)
    email:Mapped[str]=mapped_column(String , nullable=False,unique=True)
    is_active:Mapped[bool]=mapped_column(Boolean,default=True)