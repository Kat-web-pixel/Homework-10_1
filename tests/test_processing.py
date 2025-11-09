from typing import List, Dict, Any

import pytest
from src.processing import filter_by_state
from src.processing import sort_by_date

@pytest.fixture
def empty_transaction_list() -> List[Dict]:
    """Фикстура для создания пустого списка транзакций."""
    return []

@pytest.fixture
def transaction_list_without_state() -> List[Dict]:
    """Фикстура для списка транзакций без поля 'state'."""
    return [
        {'amount': 100, 'date': '2023-10-27', 'id': 1},
        {'amount': 50, 'date': '2023-10-26', 'id': 2}
    ]

def test_filter_by_state_no_matching_state(transaction_list_without_state: List[Dict]):
    """
    Проверяет, что функция возвращает пустой список, когда нет транзакций с указанным state.
    """
    filtered_transactions = filter_by_state(transaction_list_without_state, state='EXECUTED')
    assert len(filtered_transactions) == 0, "Список должен быть пустым, если нет совпадений по state"

def test_filter_by_state_empty_list(empty_transaction_list: List[Dict]):
    """
    Проверяет, что функция возвращает пустой список, если входной список транзакций пуст.
    """
    filtered_transactions = filter_by_state(empty_transaction_list, state='EXECUTED')
    assert len(filtered_transactions) == 0, "Список должен быть пустым, если входной список пуст"




@pytest.fixture
def unsorted_transaction_list() -> List[Dict]:
    """Фикстура: список транзакций в произвольном порядке."""
    return [
        {'amount': 100, 'date': '2023-10-27', 'id': 1},
        {'amount': 50, 'date': '2023-10-26', 'id': 2},
        {'amount': 200, 'date': '2023-10-28', 'id': 3},
        {'amount': 75, 'date': '2023-10-25', 'id': 4}
    ]

@pytest.mark.parametrize(
    "reverse_order, expected_first_date",
    [
        (True, '2023-10-28'),  # Сортировка по убыванию: самая поздняя дата первая
        (False, '2023-10-25') # Сортировка по возрастанию: самая ранняя дата первая
    ]
)
def test_sort_by_date_order(unsorted_transaction_list: List[Dict], reverse_order: bool, expected_first_date: str):
    """
    Проверяет правильность сортировки списка транзакций по дате в прямом и обратном порядке.
    """
    sorted_transactions = sort_by_date(unsorted_transaction_list, reverse=reverse_order)
    assert sorted_transactions[0]['date'] == expected_first_date, "Неправильный порядок сортировки"

def test_sort_by_date_missing_date(unsorted_transaction_list: List[Dict]):
    """Проверяет, что транзакции без даты не вызывают ошибку."""
    unsorted_transaction_list.append({'amount': 150, 'id': 5}) # Добавляем транзакцию без даты
    sorted_transactions = sort_by_date(unsorted_transaction_list)
    assert True  # Если дошли до сюда, значит, сортировка не вызвала исключение.