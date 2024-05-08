from fastapi import FastAPI, HTTPException, Depends
from uvicorn import run
from dependencies.database import Database, Base
from services.db_service import UserService, AccountService
from models import schemas
from dotenv import load_dotenv
import os

description = """
FinTracker
### Description

* FinTracker API is an open-source web API to help you take control of your personal finances. 
Track your income, expenses, budgets, and investments with this flexible and customizable tool.

"""

app = FastAPI(
    title="FinTracker API",
    description=description,
    version="0.1.0",
)

load_dotenv()
database = Database(os.environ['SQLALCHEMY_DATABASE_URL_DEV'])
Base.metadata.create_all(bind=database.get_engine())
user_service = UserService()
account_service = AccountService()


def get_db_session():
    session = database.get_session()
    try:
        yield session
    finally:
        session.close()


@app.get("/")
def read_root():
    return {"Hello": "World"}


@app.post("/users/", response_model=schemas.User)
def create_user(user: schemas.UserCreate, db=Depends(get_db_session)):
    if user_service.get_user_by_email(db=db, email=user.email):
        raise HTTPException(status_code=400, detail="User already exists")
    db_user = user_service.create_user(db=db, user=user)
    return db_user


@app.get("/users/", response_model=list[schemas.User])
def read_users(skip: int = 0, limit: int = 100, db=Depends(get_db_session)):
    users = user_service.get_users(db, skip=skip, limit=limit)
    return users


@app.get("/users/{user_id}", response_model=schemas.UserBase)
def read_user(user_id: int, db=Depends(get_db_session)):
    db_user = user_service.get_user(user_id=user_id, db=db)
    if db_user is None:
        raise HTTPException(status_code=404, detail="User not found")
    return db_user


# Rate limiting:
# Protect this endpoint from potential brute-force attacks attempting to guess emails.
@app.get("/users/email/{email}", response_model=schemas.User)
def read_user_by_email(email: str, db=Depends(get_db_session)):
    db_user = user_service.get_user_by_email(db=db, email=email)
    if db_user is None:
        raise HTTPException(status_code=404, detail="User not found")
    return db_user


@app.post("/users/{user_id}/accounts/", response_model=schemas.Account)
def create_account_for_user(user_id: int, account: schemas.AccountCreate, db=Depends(get_db_session)):
    return account_service.create_user_account(db=db, account=account, user_id=user_id)


@app.get("/accounts/{user_id}", response_model=list[schemas.Account])
def read_accounts(user_id: int, skip: int = 0, limit: int = 100, db=Depends(get_db_session)):
    accounts = account_service.get_accounts(db, skip=skip, limit=limit, owner_id=user_id)
    return accounts


if __name__ == "__main__":
    run("main:app", host="localhost", port=8000, reload=True)
