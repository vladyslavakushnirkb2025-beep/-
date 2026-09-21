from lib import check_password_length, format_user_data
def main():
    test_password = "mySecretPassword123"
    test_user = "  Admin_User  "
    # Викликаємо функції з модуля lib
    is_valid = check_password_length(test_password)
    formatted_name = format_user_data(test_user)
    # Виводимо результати
    print("--- Результати виконання скрипту ---")
    print(f"Користувач: {formatted_name}")
    print(f"Чи надійний пароль '{test_password}' за довжиною: {is_valid}")
if __name__ == "__main__":
    main()