from database import Base
from datetime import datetime
from sqlalchemy import Column, ForeignKey, Integer, String, Text, func
from sqlalchemy.orm import relationship,Mapped, mapped_column
class Notebook(Base):
    __tablename__="notebooks"
    id:Mapped[int]=mapped_column(Integer, primary_key=True)
    title:Mapped[str]=mapped_column(String,unique=True,nullable=False)
    created_at:Mapped[datetime]=mapped_column(server_default=func.now())
    notes:Mapped[list["Notes"]]=relationship(back_populates="notebook")
class Notes(Base):
    __tablename__="notes"
    id:Mapped[int]=mapped_column(Integer, primary_key=True)
    title:Mapped[str]=mapped_column(String,nullable=False)
    content:Mapped[str]=mapped_column(Text,nullable=False)
    notebook_id:Mapped[int]=mapped_column(ForeignKey("notebooks.id"))
    created_at:Mapped[datetime]=mapped_column(server_default=func.now())

    notebook:Mapped[Notebook]=relationship(back_populates="notes")