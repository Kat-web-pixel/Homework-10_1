from typing import Dict, List


def filter_by_state(
    transactions: List[Dict],
    state: str = 'EXECUTED'
) -> List[Dict]:
    """
    Возвращает список транзакций, у которых ключ 'state' совпадает с переданным значением.
    """
    filtered: List[Dict] = []
    for transaction in transactions:
        if transaction.get('state') == state:
            filtered.append(transaction)
    return filtered

def sort_by_date(
    transactions: List[Dict],
    reverse: bool = True
) -> List[Dict]:
    """
    Сортирует список транзакций по дате (ключ 'date') в порядке убывания или возрастания.
    """
    return sorted(transactions, key=lambda x: x.get('date', ''), reverse=reverse)

