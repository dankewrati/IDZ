def validate_password(password):
    """Перевіряє пароль за вимогами завдання 1.1."""
    if len(password) < 8:
        return False
    if not any(char.isdigit() for char in password):
        return False
    if "admin" in password.lower():
        return False
    return True
