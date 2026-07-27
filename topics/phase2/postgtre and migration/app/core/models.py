from app.core.database import Base
from sqlalchemy import ForeignKey
from sqlalchemy.orm import Mapped, mapped_column , relationship
class Customer(Base):
    __tablename__= "customers"
    __table_args__={"schema":"day_8_practice"}
    id:Mapped[int]=mapped_column(primary_key=True)
    
    email:Mapped[str]=mapped_column(unique=True,nullable=False)
    full_name:Mapped[str|None]=mapped_column(nullable=False)

    tickets:Mapped[list["Ticket"]]=relationship(back_populates="customer")
class Ticket(Base):
    __tablename__= "tickets"
    __table_args__={"schema":"day_8_practice"}
    id:Mapped[int]=mapped_column(primary_key=True)
    title:Mapped[str]=mapped_column(nullable=False)
    status:Mapped[str]=mapped_column(nullable=False)
    customer_id:Mapped[int]=mapped_column(ForeignKey("day_8_practice.customers.id"),nullable=False)
    customer:Mapped["Customer"]=relationship(back_populates="tickets")
    ticket_messages:Mapped[list["TicketMessage"]]=relationship(back_populates="ticket")
class TicketMessage(Base):
    __tablename__="ticket_messages"
    __table_args__={"schema":"day_8_practice"}
    id:Mapped[int]=mapped_column(primary_key=True)
    message:Mapped[str]=mapped_column(nullable=False)
    ticket_id:Mapped[int]=mapped_column(ForeignKey("day_8_practice.tickets.id"),nullable=False)
    ticket:Mapped["Ticket"]=relationship(back_populates="ticket_messages")