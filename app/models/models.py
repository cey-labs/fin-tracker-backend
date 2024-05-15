from sqlalchemy import Boolean, Column, ForeignKey, Integer, String, Float, Enum, DateTime
from sqlalchemy.orm import relationship
from app.dependencies.database import Base
from app.custom_types.transaction_type import TransactionType


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
    transactions = relationship("Transaction", back_populates="account")

class Transaction(Base):
    __tablename__ = "transactions"

    id = Column(Integer, primary_key=True)
    description = Column(String(512), index=True)
    amount = Column(Float, index=True)
    type = Column(Enum(TransactionType), index=True)
    timestamp = Column(DateTime, index=True)
    account_id = Column(Integer, ForeignKey("accounts.id"))

    account = relationship("Account", back_populates="transactions")
