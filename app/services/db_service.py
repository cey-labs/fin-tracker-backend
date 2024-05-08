from sqlalchemy.orm import Session
from app.models import models, schemas


class UserService:

    # Dependency injection to constructor
    def __init__(self):
        pass

    def get_user(self, db: Session, user_id: int):
        return db.query(models.User).filter(models.User.id == user_id).first()

    def get_user_by_email(self, db: Session, email: str):
        return db.query(models.User).filter(models.User.email == email).first()

    def get_users(self, db: Session, skip: int = 0, limit: int = 100):
        return db.query(models.User).offset(skip).limit(limit).all()

    def create_user(self, db: Session, user: schemas.UserCreate):
        fake_hashed_password = user.password + "notreallyhashed"
        db_user = models.User(email=user.email, hashed_password=fake_hashed_password)
        db.add(db_user)
        db.commit()
        db.refresh(db_user)
        return db_user


class AccountService:

    def __init__(self):
        pass

    def get_accounts(self, db: Session, owner_id: int, skip: int = 0, limit: int = 100):
        return db.query(models.Account).filter(models.Account.owner_id == owner_id).offset(skip).limit(limit).all()

    def create_user_account(self, db: Session, account: schemas.AccountCreate, user_id: int):
        db_account = models.Account(**account.dict(), owner_id=user_id)
        db.add(db_account)
        db.commit()
        db.refresh(db_account)
        return db_account
