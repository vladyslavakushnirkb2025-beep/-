def check_password_length(password: str) -> bool:
    """
    Перевіряє, чи довжина пароля є достатньою для базової безпеки (не менше 8 символів).
    """
    return len(password) >= 8


def format_user_data(username: str) -> str:
    """
    Форматує ім'я користувача для системного виводу.
    """
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