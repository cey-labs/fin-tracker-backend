import pytest
from pydantic import ValidationError
from app.models.schemas import UserCreate, AccountCreate

def test_user_create_schema():
    user_create = UserCreate(email="test@example.com", password="password")
    assert user_create.email == "test@example.com"
    assert user_create.password == "password"

    with pytest.raises(ValidationError) as exc_info:
        UserCreate()
    assert "email" in str(exc_info.value)
    assert "password" in str(exc_info.value)

    with pytest.raises(ValidationError) as exc_info:
        UserCreate(email="test@example.com")
    assert "password" in str(exc_info.value)

    with pytest.raises(ValidationError) as exc_info:
        UserCreate(password="password")
    assert "email" in str(exc_info.value)

def test_account_create_schema():
    account_create = AccountCreate(name="Test Account", description="Test description")
    assert account_create.name == "Test Account"
    assert account_create.description == "Test description"

    with pytest.raises(ValidationError):
        AccountCreate()