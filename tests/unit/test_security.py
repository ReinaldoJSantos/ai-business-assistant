from app.utils.security import hash_password, verify_password

def test_hash_password():
    password = "12345678"

    hashed_password = hash_password(password)

    assert hashed_password != password
    assert hashed_password.startswith("$argon2")

def test_verify_password():
    password = "12345678"

    hashed_password = hash_password(password)


    assert verify_password(password, hashed_password)


def test_verify_wrong_password():
    password = "12345678"

    wrong_password = "senha-errada"

    hashed_password = hash_password(password)

    assert not verify_password(wrong_password, hashed_password)

