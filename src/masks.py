def get_mask_card_number(card_number: str) -> str:
    """Функция, которая проверяет количество знаков в номере карты и возвращает маску"""
    if len(card_number) != 16 or not card_number.isdigit():
        raise ValueError("Номер карты должен содержать 16 цифр.")


    masked_number = f"{card_number[:4]} {card_number[4:6]}** **** {card_number[12:]}"
    return masked_number


def get_mask_account(account_number: str) -> str:
    """Функция, которая проверяет количество знаков в номере счета и возвращает маску"""
    if len(account_number) < 4 or not account_number.isdigit():
        raise ValueError("Номер счета должен содержать как минимум 4 цифры.")


    masked_account = f"**{account_number[-4:]}"
    return masked_account
