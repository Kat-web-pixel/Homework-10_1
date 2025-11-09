import pytest
from src.widget import mask_account_card
from src.widget import get_date
from datetime import datetime


@pytest.mark.parametrize(
    "input_string, expected_masked_number",
    [
        ("Visa 1234567890123456", "**** **** **** 3456"),
        ("MasterCard 9876543210987654", "**** **** **** 7654"),
        ("Счет 1234567890", "**** **** **** **** **** 67890"),
        ("Счет 5678", "**** **** **** **** **** 5678"),
    ],
)
def test_mask_account_card_correct_masking(input_string, expected_masked_number):
    result = mask_account_card(input_string)
    assert result == expected_masked_number


@pytest.fixture
def valid_date_string():
    """Фикстура с валидной датой в формате ISO."""
    return "2023-10-26T10:00:00.000000"

@pytest.mark.parametrize(
    "date_string, expected_formatted_date",
    [
        ("2023-10-26T10:00:00.000000", "26.10.2023"),  # Простая дата
        ("2024-01-01T00:00:00.000000", "01.01.2024"),  # Начало года
        ("2023-12-31T23:59:59.999999", "31.12.2023"),   # Конец года
        ("2000-02-29T12:00:00.000000", "29.02.2000"),  # Високосный год
    ],
)


def get_date(date_string: str) -> datetime:
    """Преобразует строку с датой в формате ISO в объект datetime."""
    try:
        return datetime.strptime(date_string, "%Y-%m-%dT%H:%M:%S.%f") # Явное указание формата
    except ValueError:
        raise ValueError("Invalid date format. Expected ISO format.")

@pytest.mark.parametrize(
    "invalid_date_string, expected_exception",
    [
        ("2023-13-01T00:00:00.000000", ValueError),
        ("2023-10-32T00:00:00.000000", ValueError),
        ("2023-10-26", ValueError),  # Неполный формат ISO
        ("20231026T00:00:00.000000", ValueError),  # Нет разделителей
        ("abcdefg", ValueError)
    ],
)
def test_get_date_invalid_input(invalid_date_string, expected_exception):
    """Проверяет, что функция выбрасывает ValueError для некорректных дат."""
    with pytest.raises(expected_exception):
        get_date(invalid_date_string)


















