
import uuid
import pytest
from unittest.mock import MagicMock, patch

from app.models.user import User
from app.schemas.user import UserCreate
from app.services.user import UserService


def test_create_user():
    db = MagicMock()

    user_data = UserCreate(
        name="Reinaldo",
        email="reinaldo@example.com",
        password="12345678",
    )

    created_user = User(
        name=user_data.name,
        email=user_data.email,
        password_hash="fake_hash",
    )

    with patch("app.services.user.UserRepository") as mock_repository:
        mock_repository.return_value.get_by_email.return_value = None
        mock_repository.return_value.create.return_value = created_user

        service = UserService(db)

        result = service.create_user(user_data)

        assert result.email == "reinaldo@example.com"
        assert result.name == "Reinaldo"
        assert result.password_hash != "12345678"


def test_create_user_with_existing_email():
    db = MagicMock()

    user_data = UserCreate(
        name="Reinaldo",
        email="reinaldo@example.com",
        password="12345678",
    )

    existing_user = User(
        name="Outro Usuário",
        email="reinaldo@example.com",
        password_hash="existing_hash",
    )

    with patch("app.services.user.UserRepository") as mock_repository:
        mock_repository.return_value.get_by_email.return_value = existing_user

        service = UserService(db)

        with pytest.raises(ValueError, match="Email already registered"):
            service.create_user(user_data)

            mock_repository.return_value.create.assert_not_called()

def test_get_user_by_id():
    db = MagicMock()
    user_id = uuid.uuid4()

    expected_user = User(
        id=user_id,
        name="Reinaldo",
        email="get-by-id@example.com",
        password_hash="fake_hash",
        is_active=True,
    )

    mock_repository = MagicMock()
    mock_repository.get_by_id.return_value = expected_user

    with patch(
        "app.services.user.UserRepository",
        return_value=mock_repository,
    ):
        service = UserService(db)

        result = service.get_user_by_id(user_id)

        assert result == expected_user

        mock_repository.get_by_id.assert_called_once_with(user_id)