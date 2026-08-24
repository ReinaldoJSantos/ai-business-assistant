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