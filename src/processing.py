def filter_by_state(transactions, state='EXECUTED'):

    filtered = []
    for transaction in transactions:
        if transaction.get('state') == state:
            filtered.append(transaction)
    return filtered


def sort_by_date(transactions, reverse=True):

    return sorted(transactions, key=lambda x: x.get('date', ''), reverse=reverse)