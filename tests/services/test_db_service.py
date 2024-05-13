from unittest.mock import Mock, patch
from app.models import models, schemas
from app.services.db_service import UserService, AccountService

class TestUserService:
    def test_get_user(self):
        db_mock = Mock()
        user_id = 1
        expected_user = models.User(id=user_id, email="test@example.com", hashed_password="password")
        db_mock.query.return_value.filter.return_value.first.return_value = expected_user

        user_service = UserService()

        result = user_service.get_user(db_mock, user_id)

        assert result == expected_user
        db_mock.query.assert_called_once_with(models.User)
        actual_expression = db_mock.query.return_value.filter.call_args[0][0]
        expected_expression = models.User.id == user_id
        assert str(actual_expression) == str(expected_expression)

    def test_get_user_not_found(self):
        db_mock = Mock()
        user_id = 1
        db_mock.query.return_value.filter.return_value.first.return_value = None

        user_service = UserService()

        result = user_service.get_user(db_mock, user_id)

        assert result is None
        db_mock.query.assert_called_once_with(models.User)
        actual_expression = db_mock.query.return_value.filter.call_args[0][0]
        expected_expression = models.User.id == user_id
        assert str(actual_expression) == str(expected_expression)

    def test_get_user_by_email(self):
        db_mock = Mock()
        email = "test@example.com"
        expected_user = models.User(id=1, email=email, hashed_password="password")
        db_mock.query.return_value.filter.return_value.first.return_value = expected_user

        user_service = UserService()

        result = user_service.get_user_by_email(db_mock, email)

        assert result == expected_user
        db_mock.query.assert_called_once_with(models.User)
        actual_expression = db_mock.query.return_value.filter.call_args[0][0]
        expected_expression = models.User.email == email
        assert str(actual_expression) == str(expected_expression)

    def test_get_user_by_email_not_found(self):
        db_mock = Mock()
        email = "test@example.com"
        db_mock.query.return_value.filter.return_value.first.return_value = None

        user_service = UserService()

        result = user_service.get_user_by_email(db_mock, email)

        assert result is None
        db_mock.query.assert_called_once_with(models.User)
        actual_expression = db_mock.query.return_value.filter.call_args[0][0]
        expected_expression = models.User.email == email
        assert str(actual_expression) == str(expected_expression)

    def test_get_users(self):
        db_mock = Mock()
        skip = 0
        limit = 10
        expected_users = [models.User(id=i, email=f"test{i}@example.com", hashed_password="password") for i in range(1, 6)]
        db_mock.query.return_value.offset.return_value.limit.return_value.all.return_value = expected_users

        user_service = UserService()

        result = user_service.get_users(db_mock, skip, limit)

        assert result == expected_users
        db_mock.query.assert_called_once_with(models.User)
        db_mock.query.return_value.offset.assert_called_once_with(skip)
        db_mock.query.return_value.offset.return_value.limit.assert_called_once_with(limit)

    def test_create_user(self):
        db_mock = Mock()
        user_data = schemas.UserCreate(email="test@example.com", password="password")
        expected_user_data = {
            "email": user_data.email,
            "hashed_password": user_data.password + "notreallyhashed"
        }

        user_service = UserService()

        result = user_service.create_user(db_mock, user_data)

        assert result.email == expected_user_data["email"]
        assert result.hashed_password == expected_user_data["hashed_password"]
        db_mock.add.assert_called_once_with(result)
        db_mock.commit.assert_called_once()
        db_mock.refresh.assert_called_once_with(result)

    def test_create_user_password_hashed(self):
        db_mock = Mock()
        user_data = schemas.UserCreate(email="test@example.com", password="password")
        expected_user_data = {
            "email": user_data.email,
            "hashed_password": user_data.password + "notreallyhashed"
        }

        user_service = UserService()

        result = user_service.create_user(db_mock, user_data)

        assert result.email == expected_user_data["email"]
        assert result.hashed_password == expected_user_data["hashed_password"]
        db_mock.add.assert_called_once_with(result)
        db_mock.commit.assert_called_once()
        db_mock.refresh.assert_called_once_with(result)


class TestAccountService:
    def test_get_accounts(self):
        db_mock = Mock()
        owner_id = 1
        skip = 0
        limit = 10
        expected_accounts = [models.Account(id=i, owner_id=owner_id, name=f"Account {i}", description=f"Description {i}") for i in range(1, 6)]
        db_mock.query.return_value.filter.return_value.offset.return_value.limit.return_value.all.return_value = expected_accounts

        account_service = AccountService()

        result = account_service.get_accounts(db_mock, owner_id, skip, limit)

        assert result == expected_accounts
        db_mock.query.assert_called_once_with(models.Account)
        actual_expression = db_mock.query.return_value.filter.call_args[0][0]
        expected_expression = models.Account.owner_id == owner_id
        assert str(actual_expression) == str(expected_expression)
        db_mock.query.return_value.filter.return_value.offset.assert_called_once_with(skip)
        db_mock.query.return_value.filter.return_value.offset.return_value.limit.assert_called_once_with(limit)

    def test_get_accounts_not_found(self):
        db_mock = Mock()
        owner_id = 1
        skip = 0
        limit = 10
        db_mock.query.return_value.filter.return_value.offset.return_value.limit.return_value.all.return_value = []

        account_service = AccountService()

        result = account_service.get_accounts(db_mock, owner_id, skip, limit)

        assert result == []
        db_mock.query.assert_called_once_with(models.Account)
        actual_expression = db_mock.query.return_value.filter.call_args[0][0]
        expected_expression = models.Account.owner_id == owner_id
        assert str(actual_expression) == str(expected_expression)
        db_mock.query.return_value.filter.return_value.offset.assert_called_once_with(skip)
        db_mock.query.return_value.filter.return_value.offset.return_value.limit.assert_called_once_with(limit)

    def test_create_user_account(self):
        db_mock = Mock()
        account_data = schemas.AccountCreate(name="Test Account", description="Test Description")
        user_id = 1

        account_service = AccountService()

        result = account_service.create_user_account(db_mock, account_data, user_id)

        assert result.owner_id == user_id
        assert result.name == account_data.name
        assert result.description == account_data.description
        db_mock.add.assert_called_once_with(result)
        db_mock.commit.assert_called_once()
        db_mock.refresh.assert_called_once_with(result)

    def test_create_user_account_owner_id(self):
        db_mock = Mock()
        account_data = schemas.AccountCreate(name="Test Account", description="Test Description")
        user_id = 1

        account_service = AccountService()

        result = account_service.create_user_account(db_mock, account_data, user_id)

        assert result.owner_id == user_id
        assert result.name == account_data.name
        assert result.description == account_data.description
        db_mock.add.assert_called_once_with(result)
        db_mock.commit.assert_called_once()
        db_mock.refresh.assert_called_once_with(result)