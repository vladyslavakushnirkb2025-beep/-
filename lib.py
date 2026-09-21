def validate_password_length(password: str, min_length: int = 8) -> bool:
    """
    Перевіряє, чи відповідає довжина пароля мінімальним вимогам.
    """
    return len(password) >= min_length


def format_username(username: str) -> str:
    """
    Форматує ім'я користувача до єдиного стандарту.
    """
feature-improvement
    return f"User: {username.strip().lower()}"
def greet_user(username: str) -> str:
    """
    Повертає вітальне повідомлення для користувача.
    """
    return f"Вітаємо у системі, {username}!"
def greet_user(name: str) -> str:
    """
    Повертає привітання для користувача.
    """
    return f"Вітаємо, {name}!"
    return f"User: {username.strip().lower()}"
 main
