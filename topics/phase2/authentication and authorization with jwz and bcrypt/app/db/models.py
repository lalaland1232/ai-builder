
from datetime import datetime

from app.db.database import Base
from sqlalchemy import Column, DateTime, ForeignKey, Integer, LargeBinary, String, null
from sqlalchemy.orm import relationship , Mapped , mapped_column

class User(Base):
    __tablename__="users"
    __table_args__={"schema":"prep_day10"}
    id:Mapped[int]=mapped_column(Integer,primary_key=True)
    email:Mapped[str]=mapped_column(String,unique=True,nullable=False)
    name:Mapped[str]=mapped_column(String,nullable=False)
    role_id:Mapped[int]=mapped_column(ForeignKey("prep_day10.roles.id"),default=1)

    role:Mapped["Role"]=relationship(back_populates="users")
    artifact:Mapped["Artifact"]=relationship(back_populates="user")
    refresh_tokens:Mapped[list["RefreshToken"]]=relationship(back_populates="user")

class Artifact(Base):
    __tablename__="artifacts"
    __table_args__={"schema":"prep_day10"}
    id:Mapped[int]=mapped_column(ForeignKey("prep_day10.users.id"),primary_key=True)
    artifact:Mapped[bytes]=mapped_column(LargeBinary,nullable=False)

    user:Mapped["User"]=relationship(back_populates="artifact")

class RefreshToken(Base):
    __tablename__="refresh_tokens"
    __table_args__={"schema":"prep_day10"}
    id:Mapped[int]=mapped_column(Integer,primary_key=True)
    user_id:Mapped[int]=mapped_column(ForeignKey("prep_day10.users.id"))
    hashed_token:Mapped[bytes]=mapped_column(LargeBinary,nullable=False)
    ip:Mapped[str]=mapped_column(String,nullable=False)
    created_at:Mapped[datetime]=mapped_column(DateTime,nullable=False)
    expire:Mapped[datetime]=mapped_column(DateTime,nullable=False)
    revoked_at:Mapped[datetime | None]=mapped_column(DateTime,nullable=True,default=None)
    device:Mapped[str]=mapped_column(String,nullable=True)
    user :Mapped["User"]=relationship(back_populates="refresh_tokens")

class Role(Base):
    __tablename__="roles"
    __table_args__={"schema":"prep_day10"}
    id:Mapped[int]=mapped_column(Integer,primary_key=True)
    name:Mapped[str]=mapped_column(String,nullable=False)

    users:Mapped[list["User"]]=relationship(back_populates="role")
class Permission(Base):
    __tablename__="permissions"
    __table_args__={"schema":"prep_day10"}
    id:Mapped[int]=mapped_column(Integer,primary_key=True)
    name:Mapped[str]=mapped_column(String,nullable=False)

class RolePermission(Base):
    __tablename__="role_permissions"
    __table_args__={"schema":"prep_day10"}
    id:Mapped[int]=mapped_column(Integer,primary_key=True)
    role_id:Mapped[int]=mapped_column(ForeignKey("prep_day10.roles.id"))
    permission_id:Mapped[int]=mapped_column(ForeignKey("prep_day10.permissions.id"))
