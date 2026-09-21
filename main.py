from lib import format_username, validate_password_length


def main() -> None:
    """
    Головна функція запуску скрипту.
    """
    user_name = "  Admin_User "
    test_password = "mySecretPassword123"

    formatted_user = format_username(user_name)
    is_valid = validate_password_length(test_password)

    print("--- Результати виконання скрипту ---")
    print(f"Користувач: {formatted_user}")
    print(f"Чи надійний пароль '{test_password}' за довжиною: {is_valid}")


if __name__ == "__main__":
    main()