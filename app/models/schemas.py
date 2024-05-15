from datetime import datetime
from pydantic import BaseModel


class AccountBase(BaseModel):
    name: str
    description: str | None = None


class AccountCreate(AccountBase):
    pass


class Account(AccountBase):
    id: int
    owner_id: int

    # orm_mode will tell the Pydantic model to read the data even if it is not a dict,
    # but an ORM model (or any other arbitrary object with attributes).
    class Config:
        orm_mode = True


class UserBase(BaseModel):
    email: str


class UserCreate(UserBase):
    password: str


class User(UserBase):
    id: int
    is_active: bool
    accounts: list[Account] = []

    class Config:
        orm_mode = True


class TransactionBase(BaseModel):
    amount: float
    description: str
    type: str


class TransactionCreate(TransactionBase):
    timestamp: datetime


class Transaction(TransactionBase):
    id: int
    account_id: int
    timestamp: datetime

    class Config:
        orm_mode = True
