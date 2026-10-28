from sqlalchemy import select

from app.models.user import User
from app.repositories.user import UserRepository


def test_get_user_by_email(db):
    user = User(
        name="Reinaldo",
        email="repository@example.com",
        password_hash="TEMP_HASH",
        is_active=True,
    )

    db.add(user)
    db.commit()
    db.refresh(user)

    users = db.scalars(select(User)).all()

    print("USERS:", [(u.id, u.name, u.email) for u in users])

    repository = UserRepository(db)

    result = repository.get_by_email("repository@example.com")

    print("RESULTADO:", result)

    assert result is not None
    assert result.id == user.id
    assert result.email == "repository@example.com"


def test_user_by_id(db):
    user = User(
        name="Reinaldo",
        email="repository@example.com",
        password_hash="TEMP_HASH",
        is_active = True,
    )

    db.add(user)
    db.commit()
    db.refresh(user)

    repository = UserRepository(db)
    result = repository.get_by_id(user.id)

    assert result is not None
    assert result.id == user.id
    assert result.email == user.email

def test_get_all_users(db):
    users = [
        User(
            name="Reinaldo",
            email="list-1@example.com",
            password_hash="HASH_1",
            is_active= True,
        ),
        User(
            name="Maria",
            email="list-2@example.com",
            password_hash="HASH_2",
            is_active=True,
        ),
    ]

    db.add_all(users)
    db.commit()

    repository = UserRepository(db)

    result = repository.get_all()

    assert len(result) == 2

    emails = {user.email for user in result}
    assert emails == {
        "list-1@example.com",
        "list-2@example.com",
    }