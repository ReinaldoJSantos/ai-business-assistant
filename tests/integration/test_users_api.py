from unittest.mock import MagicMock, patch
from datetime import datetime, timezone

from fastapi.testclient import TestClient

from app.main import app

client = TestClient(app)


def test_create_user():
    mock_user = MagicMock()
    now = datetime.now(timezone.utc)

    mock_user.id="12345678-1234-1234-1234-123456789012"
    mock_user.name="Reinaldo"
    mock_user.email="reinaldo@example.com"
    mock_user.is_active= True
    mock_user.created_at = now
    mock_user.updated_at = now

    """
        Durante este teste, quando o endpoint chamar UserService.create_user(), não execute o método verdadeiro. Retorne mock_user.

        ***Regra prática***
        Use patch quando você quer substituir temporariamente um comportamento real durante o teste.

        Use MagicMock quando você precisa de um objeto falso controlável.
    """
    with patch(
        "app.api.v1.users.UserService.create_user",
        return_value=mock_user,
    ):

        response = client.post(
            "api/v1/users",
            json={
                "name":"Reinaldo",
                "email":"reinaldo@example.com",
                "password":"12345678"
            },
        )
        assert response.status_code == 201
        print("STATUS:", response.status_code)
        print("JSON:", response.json())
        assert response.json()["name"] == "Reinaldo"
        assert response.json()["email"] == "reinaldo@example.com"
        assert response.json()["is_active"] is True


def test_create_user_with_invalid_email():
    response = client.post(
        "api/v1/users",

        json={
            "name":"Reinaldo",
            "email":"email-invalid",
            "password":"12345678"
    },

    )
    assert response.status_code == 422


def test_create_user_with_existing_email():
    with patch(
    "app.api.v1.users.UserService.create_user",
    side_effect=ValueError("Email already registered"),
):
        response = client.post(
            "api/v1/users",
            json={
                "name":"Reinaldo",
                "email":"reinaldo@example.com",
                "password":"12345678",
            },
        )

        assert response.status_code == 409
        assert response.json()["detail"] == "Email already registered"