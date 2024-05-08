from sqlalchemy import Boolean, Column, ForeignKey, Integer, String
from sqlalchemy.orm import relationship
from app.dependencies.database import Base
class User(Base):
    __tablename__ = "users"

    id = Column(Integer, primary_key=True)
    email = Column(String(255), unique=True, index=True)
    hashed_password = Column(String(255))
    is_active = Column(Boolean, default=True)

    accounts = relationship("Account", back_populates="owner")


class Account(Base):
    __tablename__ = "accounts"

    id = Column(Integer, primary_key=True)
    name = Column(String(255), index=True)
    description = Column(String(512), index=True)
    owner_id = Column(Integer, ForeignKey("users.id"))

    owner = relationship("User", back_populates="accounts")
