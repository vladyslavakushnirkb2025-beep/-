def validate_password_length(password: str, min_length: int = 8) -> bool:
    """
    Перевіряє, чи відповідає довжина пароля мінімальним вимогам.
    """
    return len(password) >= min_length


def format_username(username: str) -> str:
    """
    Форматує ім'я користувача до єдиного стандарту.
    """
    return f"User: {username.strip().lower()}"