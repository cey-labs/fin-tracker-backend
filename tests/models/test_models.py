from app.models.models import User, Account

def test_create_user_model():
    user = User(email="test@example.com", hashed_password="password")
    assert user.email == "test@example.com"
    assert user.hashed_password == "password"

def test_create_account_model():
    account = Account(name="Test Account", description="Test description", owner_id=1)
    assert account.name == "Test Account"
    assert account.description == "Test description"
    assert account.owner_id == 1

def test_user_account_relationship():
    user = User(email="test@example.com", hashed_password="password")
    account = Account(name="Test Account", description="Test description", owner_id=user.id)
    user.accounts.append(account)
    assert len(user.accounts) == 1
    assert user.accounts[0] == account