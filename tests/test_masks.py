import pytest
from src.masks import get_mask_card_number
from src.masks import get_mask_account

@pytest.fixture
def valid_card_number():
    """Фикстура с валидным номером карты."""
    return "1234567890123456"

@pytest.mark.parametrize(
    "card_number, expected_masked_number",
    [
        ("1234567890123456", "1234 56** **** 3456"),
        ("9876543210987654", "9876 54** **** 7654"),
    ],
)
def test_get_mask_card_number_valid_input(card_number, expected_masked_number):
    """
    Тест проверяет, что функция корректно маскирует валидные номера карт.
    Включает параметризацию для тестирования различных валидных номеров.
    """
    assert get_mask_card_number(card_number) == expected_masked_number

@pytest.mark.parametrize(
    "invalid_card_number, expected_exception, error_message",
    [
        ("1234", ValueError, "Номер карты должен содержать 16 цифр."),
        ("123456789012345", ValueError, "Номер карты должен содержать 16 цифр."),  # 15 цифр
        ("12345678901234567", ValueError, "Номер карты должен содержать 16 цифр."),  # 17 цифр
        ("abcdefghijklmnop", ValueError, "Номер карты должен содержать 16 цифр."),  # Буквы
        ("123456789012345a", ValueError, "Номер карты должен содержать 16 цифр."),  # Символы
    ],
)
def test_get_mask_card_number_invalid_input(invalid_card_number, expected_exception, error_message):
    """
    Тест проверяет, что функция выбрасывает ValueError при получении некорректного номера карты.
    Включает параметризацию для тестирования различных некорректных номеров.
    """
    with pytest.raises(expected_exception, match=error_message):
        get_mask_card_number(invalid_card_number)


@pytest.fixture
def valid_account_number():
    """Фикстура с валидным номером счета."""
    return "1234567890"

@pytest.mark.parametrize(
    "account_number, expected_masked_number",
    [
        ("1234", "**1234"),
        ("1234567890", "**7890"),
        ("5678", "**5678"),
        ("12345", "**2345"),
    ],
)
def test_get_mask_account_valid_input(account_number, expected_masked_number):
    """
    Этот тест проверяет, что функция корректно маскирует валидные номера счетов.
    Используется параметризация для тестирования различных валидных номеров.
    """
    assert get_mask_account(account_number) == expected_masked_number

@pytest.mark.parametrize(
    "invalid_account_number, expected_exception, error_message",
    [
        ("123", ValueError, "Номер счета должен содержать как минимум 4 цифры."),  # Меньше 4 цифр
        ("abcd", ValueError, "Номер счета должен содержать как минимум 4 цифры."),   # Буквы
        ("12a3", ValueError, "Номер счета должен содержать как минимум 4 цифры."),   # Буквы и цифры
         ("", ValueError, "Номер счета должен содержать как минимум 4 цифры."),    # Пустая строка
    ],
)
def test_get_mask_account_invalid_input(invalid_account_number, expected_exception, error_message):
    """
    Этот тест проверяет, что функция выбрасывает ValueError при получении некорректного номера счета.
    Используется параметризация для тестирования различных некорректных номеров.
    """
    with pytest.raises(expected_exception, match=error_message):
        get_mask_account(invalid_account_number)